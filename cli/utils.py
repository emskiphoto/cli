# utils.py
from pandas import read_csv

# functions that are used in the main.py script
def say_hello_utils():
    print('Hello from the Utils.py module')
    
def pd_read_csv(file_in):
    return read_csv(file_in)

