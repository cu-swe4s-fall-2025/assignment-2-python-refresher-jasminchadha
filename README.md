[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

# Continuous Integration and Best Practices (10/07/2025)
1. Restructured repo to include an src folder that houses all source code. Edited associated files to ensure they include the right path.
2. Implemented autoamted testing using github actions for when any branch is pushed, a pull request is made on the master branch, unit and functional tests, and PEP8 style checks.

# Creating test_my_utils.py and test_print_fires.sh (09/30/2025)
1. test_my_utils.py: created unit tests with randomness and positive and negative values for mean, median, and standard deviation functions in my_utils.py.
2. test_print_fires.sh: created a test data file to use Stupid Simple BaSh Testing that includes functional tests for exit codes and different operations in print_fires.py.

# Updating my_utils.py and print_fires.py (09/30/2025)
1. my_utils.py: added new functions to find the mean, median, and standard deviation for an array of integers.
2. print_fires.py: added a command line argument to specify an operation (mean, median, standard deviation) for the returned array.

# Updating print_fires.py, my_utils.py, and run.sh (09/15/2025)
1. Utilized argparse to pass in function arguments via the command line in print_fires.py. Added main function to print_fires.py. Added documentation for main function.
2. Updated the function get_column in my_utils.py to convert all values in resultsarray to integers. Added exceptions to throw errors for incorrect file reading or integer conversion. Added documentation for get_column function.
3. Updated run.sh to use command line arguments in print_fires.py: 1 example works and 2 examples throw errors.

# Creating run.sh file (09/09/2025)
1. Created run.sh file to run print_fires.py using bash.

# Second editing of my_utils.py and print_fires.py (09/09/2025)
1. Edited my_utils.py: Changed the input of the result column in get_column() to be a named argument that defaults to 1.
2. Edited print_fires.py: Changed the function call of get_column() so result_column = fires_column due to the change to a named argument.

# First editing of my_utils.py and print_fires.py (09/09/2025)
1. Edited my_utils.py: created function get_column(), which takes the inputs of a file name, a query column, a query value, and a result column. This function will read in a file line by line, and create an array for each line. Then it will check if the query value matches the query column, and if it does, it will store the associated value in the result column in an array that is returned.
2. Edited print_fires.py: fixed syntax errors and correctly imported the function get_column() so it could be correctly called. Called the function to report the values of CO2 emissions associated with forest fires in the United States of America throughout this data set. 