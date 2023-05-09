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

## Examples

### Output the five largest entries
```
$ tar tzvf ORCID_2022_10_summaries-000.tar.gz | taru -h | head -5
425793331       ORCID_2022_10_summaries
423597236       ORCID_2022_10_summaries/000
1181208 ORCID_2022_10_summaries/897
759861  ORCID_2022_10_summaries/013
250719  ORCID_2022_10_summaries/004
```

### Output the sum all file sizes in human-readable form
```
$ tar tzvf ORCID_2022_10_summaries-000.tar.gz | taru -sh
406.1MiB        total
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
