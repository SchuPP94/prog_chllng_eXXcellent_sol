'''
This file contains the class which handles the class reading for the programming challenge.

The class will have a handler function, which automatically chooses which reader to take.

New file types can then be added by expanding the class with new reading methods and adding them 
to the handler function. Alternatively the correct reading function can be chosen directly.
'''
import os
import numpy as np

class ReadData:
    def __init__(self):
        self.checked = False

    def read_file(self):
        pass

    def read_csv(self, path_to_file, headline = False):
        if not self.checked:
            data_type = path_to_file.split('.')[-1]
            if data_type != 'csv':
                print('Error: File has the wrong format!')
                return None, None

        if not os.path.exists(path_to_file):
            print('Error: The file does not exist!')
            return None, None

        lines = []
        with open(path_to_file, 'r') as fid:
            for line in fid:
                lines.append(line)
        
        data_start_row = 0
        data_names = None
        if headline:
            data_names = np.asarray(lines[0].split(','))
            data_start_row = 1
        
        data = np.zeros((len(lines)-data_start_row, len(data_names)), dtype = np.float)
        for idx in range(len(lines)-data_start_row):
            data[idx, :] = np.asarray(lines[idx + data_start_row].split(',')).astype(np.float)

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
