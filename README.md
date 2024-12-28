# pycli
Basic Command-Line Interface (CLI) script that reads a local CSV and writes a modified version back to disk with a new name from a single CLI command.

## Installation Instructions
The following method uses pipx for installation which generates a command line (terminal) command 'pycli'.  The 'pycli' command can be run from any directory on the computer.

1. Obtain Code<BR>
    a. Simple download….<BR>
    b. git clone https://github.com/emskiphoto/pycli.git
2. Install Python (version 3.8 or newer) - https://www.python.org/downloads/#:~:text=Looking%20for%20a%20specific%20release%3F
3. Install pipx <BR>
    Windows:  
    `py -m pip install --user pipx`<BR>
    `py -m pipx ensurepath`<BR>
    Unix/macOS:<BR>
    `python3 -m pip install --user pipx`<BR>
    `python3 -m pipx ensurepath`<BR>
4. `pipx install pycli`

## Usage
$ cli 'data/test_file.csv'

## Background
This repository is intended to be used as a template for development of CLI packages.  Main.py holds the primary code and is the entry point of the script.  Utils.py contains functions.  Config.py contains configuration items.  It includes a separate 'data' directory containing input data.  This repo has only been tested on Windows OS.

## Reference
https://github.com/trstringer/pycli

