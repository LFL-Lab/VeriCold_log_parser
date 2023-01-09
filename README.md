# VeriColdLogFile (.vcl) Parser and CSV Converter Toolkit

Oxford Instruments Dilution Refridgerators with Triton Systems generate log files in `.vcl` format. This tool converts them into `.csv` for any analysis needs.

## Installation:

```bash
$ git clone https://github.com/shanto268/VeriCold_log_parser.git
$ cd VeriCold_log_parser
$ pip install -r requirements.txt
```

## Usage:

```bash
usage: convertVCL.py [-h] [--file FILE] [--all ALL]

Conversion tool from .vcl files to .csv for Oxford Instrument Dilution Refridgerators with Triton System

options:
  -h, --help   show this help message and exit
  --file FILE  convert the .vcl file argument (FILE) to .csv
  --all ALL    converts all files in the path argument (ALL)
```

### Examples:

```bash
python convertVCL.py --all path/to/all/vcl/files
```

```bash
python convertVCL.py --file path/to/a/vcl/file
```
