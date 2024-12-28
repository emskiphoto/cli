# main.py
# This script is the entry point for the overall python module.

# Copyright emskiphoto - December 21, 2024
# https://github.com/emskiphoto

# this module contains a basic CLI script that reads a local CSV
# and writes a modified version back to disk with a new name
# script can take in multiple command line arguments
# a 'test_file.csv' is saved in 'data' as a convenience to support testing

import argparse
from pandas import read_csv
from .utils import *
from .config import *

def main():
    #     test say_hello_utils function from utils.py
    say_hello_utils()
#     what is filename, frequency?
    print(args.filename)
    print(args.frequency)
#     at this point the args.frequency variable doesn't actually do anything - just print it for now
    if args.frequency != None:
        if args.frequency != 'H':
#             use the freqstr_frequency dictionary from config.py
            print(f'Resamplng at "{freqstr_frequency[args.frequency]}" frequency')

# Open a .CSV file in 'data' folder 
# what is the name of the file that should be opened from the data folder?
    file_in = args.filename
    file_out = file_in.replace('.csv', '_shuffled.csv')
    
#     df = read_csv(file_in)
    df = pd_read_csv(file_in)
#     shuffle order of table
    print(df.head())
    print('\nshuffling table order at random\n')
    df = df.sample(df.shape[0])
# Write .CSV file to 'data' folder 
    print('\n', df.head(), '\n')
    df.to_csv(file_out)
    print(f'\nsaving {file_out} to disk\n')
    

# read arguments provided in command line statement
parser = argparse.ArgumentParser(description='Open a CSV file.')
# required argument 'filename'
parser.add_argument('filename', help='The CSV file to open')
# To make an argument optional in argparse, you simply need to add a prefix to the argument name, typically either a single hyphen (-) or a double hyphen (--)
# optional argument 'frequency'
parser.add_argument('-frequency', type=str, help='Frequency of output data')
# compile list of args
args = parser.parse_args()

# activate the script - this step initiates execution of module using CLI arguments
if __name__ == '__main__':
    main()
    
    