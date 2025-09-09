[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

# First editing of my_utils.py and print_fires.py (09/09/2025)
1. Edited my_utils.py: created function get_column(), which takes the inputs of a file name, a query column, a query value, and a result column. This function will read in a file line by line, and create an array for each line. Then it will check if the query value matches the query column, and if it does, it will store the associated value in the result column in an array that is returned.
2. Edited print_fires.py: fixed syntax errors and correctly imported the function get_column() so it could be correctly called. Called the function to report the values of CO2 emissions associated with forest fires in the United States of America throughout this data set. 

# Second editing of my_utils.py and print_fires.py (09/09/2025)
1. Edited my_utils.py: Changed the input of the result column in get_column() to be a named argument that defaults to 1.
2. Edited print_fires.py: Changed the function call of get_column() so result_column = fires_column due to the change to a named argument.

# Creating run.sh file (09/09/2025)
1. Created run.sh file to run print_fires.py using bash.