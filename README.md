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
```sh
taru --help
```
