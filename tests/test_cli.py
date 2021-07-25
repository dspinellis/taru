#
# Copyright 2021 Diomidis Spinellis
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

from taru import cli
from types import SimpleNamespace


def test_humanize():
    assert cli.humanize(1, 1000) == '1B'
    assert cli.humanize(999, 1000) == '999B'
    assert cli.humanize(1000, 1000) == '1.0kB'

    size = 1024
    assert cli.humanize(size, 1024) == '1.0kiB'
    assert cli.humanize(size * 2, 1024) == '2.0kiB'
    assert cli.humanize(size * 2.5, 1024) == '2.5kiB'

    size *= 1024
    assert cli.humanize(size, 1024) == '1.0MiB'

    size *= 1024
    assert cli.humanize(size, 1024) == '1.0GiB'

    size *= 1024
    assert cli.humanize(size, 1024) == '1.0TiB'

    size *= 1024
    assert cli.humanize(size, 1024) == '1.0PiB'

    size *= 1024
    assert cli.humanize(size, 1024) == '1.0EiB'

    size *= 1024
    assert cli.humanize(size, 1024) == '1.0ZiB'

    size *= 1024
    assert cli.humanize(size, 1024) == '1.0YiB'


def test_read_input():
    root = 'drwxr-x--- dds/dds       10 2021-07-14 11:41 home/'
    dir1 = 'drwxr-x--- dds/dds       5 2021-07-14 11:41 home/dds/'
    file1 = '-rwxr-x--- dds/dds       20 2021-07-14 11:41 home/dds/file1'
    file2 = '-rwxr-x--- dds/dds      100 2021-07-14 11:41 home/dds/file2'
    dir2 = 'drwxr-x--- dds/dds       1 2021-07-14 11:41 home/dds/src/'

    args = SimpleNamespace()
    args.separate_dirs = False
    args.all = False

    # Empty
    (sizes, total) = cli.read_input(args, [])
    assert total == 0
    assert len(sizes) == 0

    # Not standalone files
    (sizes, total) = cli.read_input(args, [root, dir1, file1])
    assert total == 35
    assert len(sizes) == 2
    assert sizes['home'] == 35
    assert sizes['home/dds'] == 25

    # Include standalone files
    args.all = True
    args.separate_dirs = False
    (sizes, total) = cli.read_input(args, [root, dir1, file1])
    assert total == 35
    assert len(sizes) == 3
    assert sizes['home'] == 35
    assert sizes['home/dds'] == 25
    assert sizes['home/dds/file1'] == 20

    # No recursive directory sums
    args.all = False
    args.separate_dirs = True
    (sizes, total) = cli.read_input(args, [root, dir1, dir2, file1, file2])
    assert len(sizes) == 3
    assert total == 136
    assert sizes['home'] == 15
    assert sizes['home/dds'] == 126

    # No recursive directory sums; all files
    args.all = True
    args.separate_dirs = True
    (sizes, total) = cli.read_input(args, [root, dir1, dir2, file1, file2])
    assert len(sizes) == 5
    assert total == 136
    assert sizes['home'] == 15
    assert sizes['home/dds'] == 126
    assert sizes['home/dds/file1'] == 20
    assert sizes['home/dds/file2'] == 100
    assert sizes['home/dds/src'] == 1
