'''
This file contains the class which handles the class reading for the programming challenge.

The class will have a handler function, which automatically chooses which reader to take.

New file types can then be added by expanding the class with new reading methods and adding them 
to the handler function. Alternatively the correct reading function can be chosen directly.
'''
import os
import numpy as np

def isInt(in_string):
    '''
    Checks, whether the string input can be converted to int.
    If yes, it returns True, otherwise it returns False
    Inputs:
        in_string:  string to be checked for convertability
    Returns:
        True or False Statement, whether the string can be converted
    '''
    # Managed via a try except structure. Tries to convert the string and catches 
    # the Value Error, meaning that if no conversion is possible, the string does not 
    # convert to int
    try:
        int(in_string)
        return True
    except ValueError:
        return False

def isFloat(in_string):
    '''
    Checks, whether the string input can be converted to float.
    If yes, it returns True, otherwise it returns False
    Inputs:
        in_string:  string to be checked for convertability
    Returns:
        True or False Statement, whether the string can be converted
    '''
    # Managed via a try except structure. Tries to convert the string and catches 
    # the Value Error, meaning that if no conversion is possible, the string does not 
    # convert to float

    try:
        float(in_string)
        return True
    except ValueError:
        return False

def getType(in_string):
    '''
    Checks for the different possible types in which to convert the string.
    If one of the conversions is possible, the string gets converted and the new 
    typed value gets returned. If not conversion is possible, the string itself is returned
    Supports currently int, float and string data types
    Inputs:
        in_string:  String to be converted
    Returns:
        The converted value
    '''
    # Check if in_string is int. If yes, convert it to int and return
    if isInt(in_string):
        return int(in_string)
    # Check if in_string is float. If yes, convert it to float and return
    elif isFloat(in_string):
        return float(in_string)
    # Return the input value, if no conversion is possible
    else:
        return in_string

def convert_list_types(in_list):
    '''
    Perform data type conversions on all elements of a list and return the completely converted
    list. No sanity check is performed, whether the list only contains strings.
    Inputs:
        in_list:    List of the Input values, should be all in string format
    Returns:
        List of the input values converted to their corresponding data types for further evaluation
    '''
    # Create the empty output list and iterate over the elements in the input list
    out_list = []
    for elem in in_list:
        # Append the converted input value
        out_list.append(getType(elem))
    # return the converted list
    return out_list

class ReadData:
    '''Class for Reading in the Data
    
    This class handles all functions regarding the reading in of data
    If a new format needs to be defined, a new function for the new data type can be written 
    The functions for sanity checks are defined separately for better readability and to 
    reduce the amount of written code
    '''
    def __init__(self):
        '''
        Initialize the Class.
        Currently only one variable is set by default. Later the class could be expanded
        to take the path to the file as input and to perform the sanity checks already
        once for all functions
        '''
        self.checked = False

    def _check_format(self, file_name, format_name):
        '''
        Performs the sanity check, whether the given file is of the given data format
        Inputs:
            file_name:  Name of the file. Must be string
            format_name:    Name of the wished format. Must be string
        Returns:
            A boolean value representing, whether the format is correct
        '''
        # Check whether the file name contains a '.' --> if not, it is not a file
        if '.' not in file_name:
            print('Error: Path does not point to a file!')
            return False
        # Split the name at the '.' and take the last part --> this is the file format
        file_format = file_name.split('.')[-1]
        
        # Check whether the actual file format and the wished format are equal
        if file_format != format_name:
            print('Error: File does not have the correct format!')
            return False
        else:
            return True
   
    def read_file(self):
        '''
        Reads the data of the file to which the path points to and reads it
        Chooses the correct reader depending on the ending of the file or the specified 
        data type

        Inputs:
            path_to_file:   path to the file at which the data is stored. String format.
            headline:   Boolean variable. Defines, whether the file contains column names in the 
                    first line of the file
            file_format:    format of the given file. If given, chooses the correct reader function
                    based on the given value. Currently only 'csv' is supported, but other formats can
                    be included
            Returns:
                One numpy array with the names of the values given in the table and another numpy array
                containing the data. Value names correspond to the columns of the matrix.
        '''
        pass

    def read_csv(self, path_to_file, headline = False):
        '''
        Reads the data of a csv-file given in the path in the input. If the file does not exist
        or is not in the csv format, an error message is printed and None arrays are returned.
        Inputs:
            path_to_file:   path to the dile at which the data is stored. String format.
            headline:   Boolean variable. Defines, whether the file contains the value names in the first row 
                    of the table
        Returns:
            One numpy array with the names of the values given in the table and another numpy array
            containing the data. Value names correspond to the columns of the matrix
        '''
        # Check whether the path is of the correct format, only if it was not already checked
        if not self.checked:
            # Check the format
            correct_format = self._check_format(path_to_file, 'csv')
            # return None values if not in the right format
            if not correct_format:
                return None, None

        # Check, whether the file exists using the os library --> if not return None values
        if not os.path.exists(path_to_file):
            print('Error: The file does not exist!')
            return None, None

        # Create a list for reading in the file line by line
        lines = []
        with open(path_to_file, 'r') as fid:
            for line in fid:
                # Use the rstrip method inbuilt in python to remove newline and trailing whitespace
                lines.append(line.rsplit('\n')[0])
                print(lines[-1])
        
        # Create the variable to store the column names in and a counter variable, 
        # marking whether the first line was taken as headline or not
        data_start_row = 0
        data_names = None
        if headline:
            # Split the first line at every ',', as the format is csv
            data_names = lines[0].split(',')
            # Set data_start_row to one to skip the first line for the data matrix
            data_start_row = 1
        
        # Create the empty list of data and go over the remaining data points
        data = []
        for idx in range(len(lines)-data_start_row):
            # Transform the data points to their respective types and append them to the list
            # of data. 
            data.append(convert_list_types(lines[idx + data_start_row].split(',')))

        return data_names, data

def main():
    print("Hello World")
    test_class = ReadData()

    path_to_file = '/mnt/c/Users/Philipp/Documents/exxcellent_solutions/prog_chllng_eXXcellent_sol/resources/weather.csv'
    data_names, data = test_class.read_csv(path_to_file, True)
    print(data_names)
    print(data)

if __name__ == '__main__':
    main()
