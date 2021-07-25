# Tar Space Usage

Taru processes a tar listing to display the cumulative size of files
stored in individual directories.
Its output and options are similar to the Unix disk usage _du_(1) command.


# Installation

## Using Pip
```sh
pip install taru
```

## Manual
```sh
git clone https://github.com/dspinellis/taru
cd taru
python setup.py install
```

# Usage

## Example:
```
tar tzvf file.tar.gz | taru
```

## Available command-line options
```
$ taru --help

usage: taru [-0] [-a] [-c] [-h] [-i] [-S] [-s] [-?]

taru usage

optional arguments:
  -0, --null            End output lines with a null character rather than
                        newline
  -a, --all             Output all files, not just directories
  -c, --total           Output a grand total
  -h, --human-readable  Output sizes in human-readable format using powers of
                        1024
  -i, --si              Output sizes in human-readable format using powers of
                        1000
  -S, --separate-dirs   Do not include size of subdirectories
  -s, --summarize       Output only the total size of all files
  -?, --help            Display this help message
```
