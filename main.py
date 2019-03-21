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
    '''
    Concatenate a path and a filename to form the complete path to the file to be read.
    Inputs:
        path_name:  Name of the path in which the dataset is
        file_name:  Complete name of the file to be read
    Returns_
        The concatenated pathname
    '''
    # Check, whether the path ends with '/' --> if not, append it to the path
    if path_name[-1] != '/':
        path_name = path_name + '/'
    # concatenate and return
    return path_name + file_name

# Variables for starting the program
# resource path points to the directory, at which the datasets are stored, dataset is the filename of the
#dataset to be evaluated and column1 and column2 are the names/indices of the columns to be evaluated
resource_path = '/mnt/c/Users/Philipp/Documents/exxcellent_solutions/prog_chllng_eXXcellent_sol/resources'
dataset = 'football.csv'

column1 = 'Goals'
column2 = 'Goals Allowed'

def main():
    '''
    Main of the programming challenge
    '''
    # First create an object of the data reader class
    data_reader = ReadData()
    # create the complete path
    complete_path = path_concat(resource_path, dataset)
    # read the data from the file
    data_names, data = data_reader.read_csv(complete_path, True)
    
    # Create the evaluation class
    eval_class = EvalData(data_names, data)
    # Get the column value to be printed at the row with the smallest difference
    smallest_row = eval_class.get_smallest_diff(column1, column2, 0)

    # print the results
    print('Dataset: {0}'.format(dataset))
    print('The smallest difference between {0} and {1} was at: {2}'.format(column1, column2, smallest_row))

if __name__ == '__main__':
    main()
