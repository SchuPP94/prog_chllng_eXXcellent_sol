'''
File containing the class definition of the evaluation of the given data. Will be filled with 
content soon.
'''

class EvalData:
    def __init__(self, data_names, dataset):
        self.data_names = data_names
        self.dataset = dataset

    def get_data_col(self, col_id):
        '''
        Returns the complete column of the dataset indicated by the given column ID. This can 
        not be done via slicing, as the dataset is a nested list due to the possible differing
        data types of the row elements
        Inputs:
            col_id: Index of the column to extract
        Returns:
            All the Values of the column in a list
        '''
        # Check, whether the Index is a integer or not. If not return None and print an Error message
        if not isinstance(col_id, int):
            print('Error: ID is not integer!')
            return None
        # Create the empty column list and iterate over all rows of the dataset
        column = []
        for row in self.dataset:
            # Append the element indicated by col_id to the output list
            column.append(row[col_id])
        # Return the column
        return column

    def get_col_idx(self, col):
        '''
        Transform the given column value to an index for the dataset matrix. If it is
        equal to one of the names of the data column names, return the corresponding index.
        If it is already an index, return the input.
        Else print an error message and return None.
        Inputs:
            col:    Name or Inde of the column from the dataset
        Returns:
            The final index value of the dataset matrix
        '''
        # If it is already integer, just return the input
        if isinstance(col, int):
            return col
        elif isinstance(col, str):
            # Return the index of the position, at which the column name matches one element of 
            # the dataset names
            col_idx = [pos for pos in range(len(self.data_names)) if self.data_names[pos]==col]
            if len(col_idx) == 0:
                print('Error: Element {0} is not contained in the dataset'.format(col))
                return None
            else:
                return col_idx[0]
        # If it is no supported datatype return None and print an error message
        else:
            print('The type for the column {0} is not supported!'.format(col))
            return None

    def get_smallest_diff(self, col1, col2, return_col=None, use_abs=True):
        '''
        Return the smallest difference value between 2 columns of the dataset in the class
        The columns can be integer indices or the names of the columns.
        Inputs:
            col1:   Value indicating the first column of the dataset to compare to
            col2:   Value indicating the second column of the dataset to compare to
        Returns:
            The value of the row with the smallest difference, which return_col indicates
            If return_col is set to None, automatically the first value gets returned
        '''
        data_col1 = self.get_data_col(self.get_col_idx(col1))
        data_col2 = self.get_data_col(self.get_col_idx(col2))
        if data_col1 is None or data_col2 is None:
            return None

        min_idx = 0
        min_val = 100000
        for i in range(len(data_col1)):
            diff = data_col1[i] - data_col2[i]
            if use_abs:
                diff = abs(diff)
            if diff < min_val:
                min_idx = i
                min_val = diff

        if return_col is not None:
            return_idx = self.get_col_idx(return_col)
            return self.dataset[min_idx][return_idx]
        else:
            return self.dataset[min_idx][0]
