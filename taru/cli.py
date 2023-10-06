#!/usr/bin/env python3
#
# Copyright 2021-2023 Diomidis Spinellis
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
List the size of directories in a tar file
"""

import argparse
import re
import signal
import sys

TAR_LINE = re.compile(
    r'.{10}\s+[^/]+/[^\s]+\s+(\d+) \d{4}-\d\d-\d\d \d\d:\d\d (.*)'
)


def humanize(num, power):
    """Return the number in units of power with the corresponding suffix"""
    num = int(num)
    if num < power:
        return f'{num}B'
    suffix = 'B' if power == 1000 else 'iB'
    for unit in ['k', 'M', 'G', 'T', 'P', 'E', 'Z']:
        num /= power
        if num < power:
            return "%3.1f%s%s" % (num, unit, suffix)
    num /= power
    return "%.1fY%s" % (num, suffix)


def read_input(args, input_stream):
    """Return a dictionary and total of the tar data sizes read from the
    provided input stream."""

    path_size = {}
    total_size = 0

    # Accumulate size of files stored in each path part
    for line in input_stream:
        matched = TAR_LINE.match(line)
        if not matched:
            print(f"Unable to match {line}", file=sys.stderr)
            continue
        size = int(matched.group(1))
        total_size += size
        name = matched.group(2)
        is_dir = (line[0] == 'd')
        components = name.split('/')
        if is_dir:
            del components[-1]

        # Iterate over path components, with i counting the current number
        path = ''
        i = -1
        components_number = len(components)
        for element in components:
            i += 1
            if path:
                path += '/' + element
            else:
                path = element
            # If separate_dirs, only add to parent directory
            if args.separate_dirs and i < components_number - 2:
                continue
            # Don't tally standalone files unless --all is specified
            if not args.all and not is_dir and i == components_number - 1:
                continue
            if path in path_size:
                path_size[path] += size
            else:
                path_size[path] = size
    return (path_size, total_size)


def display_sizes(args, path_size, size_format):
    """Display the size of each stored element"""

    eol = "\0" if args.null else "\n"

    # Print the paths ordered by size
    for k in sorted(path_size, key=path_size.get, reverse=True):
        print(size_format(path_size[k]), k, sep="\t", end=eol)


def main():
    """Program entry point"""
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

    parser = argparse.ArgumentParser(description='taru usage',
                                     add_help=False)
    parser.add_argument('-0', '--null',
                        help=('End output lines with a null character rather'
                              ' than newline'),
                        action='store_true')

    parser.add_argument('-a', '--all',
                        help='Output all files, not just directories',
                        action='store_true')

    parser.add_argument('-c', '--total',
                        help='Output a grand total',
                        action='store_true')

    parser.add_argument('-h', '--human-readable',
                        help=('Output sizes in human-readable format using'
                              ' powers of 1024'),
                        action='store_true')

    parser.add_argument('-i', '--si',
                        help=('Output sizes in human-readable format using'
                              ' powers of 1000'),
                        action='store_true')

    parser.add_argument('-S', '--separate-dirs',
                        help='Do not include size of subdirectories',
                        action='store_true')

    parser.add_argument('-s', '--summarize',
                        help='Output only the total size of all files',
                        action='store_true')

    parser.add_argument('-?', '--help',
                        help='Display this help message',
                        action='store_true')

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        sys.exit(0)

    # Setup size output function
    if args.human_readable:
        def size_format(x): return humanize(x, 1024.0)
    elif args.si:
        def size_format(x): return humanize(x, 1000.0)
    else:
        def size_format(x): return x

    (sizes, total) = read_input(args, sys.stdin)

    if not args.summarize:
        display_sizes(args, sizes, size_format)

    if args.total or args.summarize:
        print(size_format(total), "\ttotal")


if __name__ == "__main__":
    main()
