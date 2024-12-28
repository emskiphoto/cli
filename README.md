# cli
Basic Command-Line Interface (CLI) script that reads a local CSV and writes a modified version back to disk with a new name

## Installation Instructions
1. Obtain Code<BR>
    a. Simple download….<BR>
    b. git clone https://github.com/emskiphoto/cli.git
2. Install Python
3. Install pipx <BR>
    Windows:  
    `py -m pip install --user pipx`<BR>
    `py -m pipx ensurepath`<BR>
    Unix/macOS:<BR>
    `python3 -m pip install --user pipx`<BR>
    `python3 -m pipx ensurepath`<BR>
4. `pipx install cli`


## Usage
$ cli 'data/test_file.csv'

## Background
This repository is intended to be used as a template for development of CLI packages.  Main.py holds the primary code and is the entry point of the script.  Utils.py contains functions.  Config.py contains configuration items.  It includes a separate 'data' directory containing input data.  This repo has only been tested on Windows OS.
