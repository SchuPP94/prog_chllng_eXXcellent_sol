'''
main file for the eXXcellent solutions programming challenge

Author: Philipp Schulz;
Start: 20. March 2019
End:
'''
import numpy as np
from read_data.read_data import ReadData

def path_concat(path_name, file_name):
    if path_name[-1] != '/':
        path_name = path_name + '/'

    return path_name + file_name

resource_path = '/mnt/c/Users/Philipp/Documents/exxcellent_solutions/prog_chllng_eXXcellent_sol/resources'
dataset = 'weather.csv'

def main():
    data_reader = ReadData()

    data_names, data = data_reader.read_csv(path_to_file, True)

if __name__ == '__main__':
    main()
