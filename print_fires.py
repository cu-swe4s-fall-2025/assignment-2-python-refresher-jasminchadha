# Import my_utils with the get_column function
import my_utils

# Define inputs from file for function
country = 'United States of America'
country_column = 0
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'

# Call function and print results
fires = my_utils.get_column(file_name, country_column, country,
                            result_column=fires_column)
print(fires)
