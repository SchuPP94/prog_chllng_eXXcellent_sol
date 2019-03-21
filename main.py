'''
main file for the eXXcellent solutions programming challenge

Author: Philipp Schulz;
Start: 20. March 2019
End:
'''
import numpy as np
from read_data.read_data import ReadData
from evaluate_data.base_evaluation import EvalData

def path_concat(path_name, file_name):
    if path_name[-1] != '/':
        path_name = path_name + '/'

    return path_name + file_name

resource_path = '/mnt/c/Users/Philipp/Documents/exxcellent_solutions/prog_chllng_eXXcellent_sol/resources'
dataset = 'football.csv'

column1 = 'Goals'
column2 = 'Goals Allowed'

def main():
    data_reader = ReadData()
    complete_path = path_concat(resource_path, dataset)
    data_names, data = data_reader.read_csv(complete_path, True)

    eval_class = EvalData(data_names, data)

    smallest_row = eval_class.get_smallest_diff(column1, column2, 0)
    print('Dataset: {0}'.format(dataset))
    print('The smallest difference between {0} and {1} was at: {2}'.format(column1, column2, smallest_row))

if __name__ == '__main__':
    main()
