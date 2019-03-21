# prog_chllng_eXXcellent_sol
This Readme contains the instructions on how to execute the program and some additional details/thoughts i had in mind while designing the code. First to start, you need python 3.5.2 or higher. Before you start, use any texteditor and open the main.py file. In there you will find 4 variables which are named 'resource_path', 'dataset', 'column1' and 'column2'. You need to adjust these variables for you to run the program. First change the path given in 'resource_path' to the path at which you are saving the dataset. Then change the name of the dataset given in 'dataset' to the one you want to evaluate. Right now, only csv datasets are supported, but you can choose any dataset you like (Also new ones). 'column1' and 'column2' need to be set to either the names or the column indices of the dataset, which you want to compare to each other. 

After that, execute 'python main.py' and the program will print the first element of the row with the smallest difference of the two columns on the console. 

## Additional Thoughts
Reading of the data is written as a class, in which different methods can be included. Right now, only reading in of csv files is supported, but later additional formats could be included as additional methods. There is also a method included, which can be used to automatically take the right format for reading in the files. Right now the data is returned as two lists, one containing the names of the tables, the other containing each row of the table as a list. This format could be adapted, so that other data files are easier to include. However, this format is very good for tables of data, which is why it was used here.
There are also some utility functions there, which are used to automatically determine the needed datatype of the column of the table and to read the data in the correct data types. With this, no additional definition of the data types of the columns is needed, if different data types are contained in the table.
The EvalData class calculates saves the dataset and the data_names as class variables. The calculation of the smallest difference here is a class member variable, but as the name of the file suggests, it is thought of as a base class, which handles the basic dataset convenience functions (like searching for certain columns and managing the database). This class could be inherited by other classes, which then add new functionalities, depending on the task to be performed. If for example another evaluation is needed, where database sorting based on a certain column might be needed, a new class could be created, which inherits the EvalData class and adds new sorting functionalities. As this would unnecessarily increase the project, it was omitted for this challenge.
Finally, I tried to separate the functions into smaller subfunctions, which might be useful at other places for other purposes. This might lead to blown up files, but on the other hand makes maintainability easier, as everything is structured and improves readability of separate methods, as it reduces the needed code per block.
