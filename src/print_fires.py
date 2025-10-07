# Import packages and files
import argparse
import my_utils


def main():
    """
    Prints the values of CO2 emissions associated with forest fires
    in the United States of America throughout a data set.

    Args:
    file_name (str): Name of the file.
    country_column (int): Column number in the data set
                          associated with country names.
    country (str): Name of the country.
    fires_column (int): Column number in the data set
                        associated with forest fires.
    operation (str): Name of operation to do for array:
                     mean, median, or sd.

    Returns:
    fires (int): An array of all forest fire emissions
                 associated with a country in this data set.
    mean_val (float): Mean of the array (if operation is chosen).
    median_val (float): Median of the array (if operation is chosen).
    sd_val (float): Standard deviation of the array (if operation is chosen).
    """

    # Set up argument parser
    parser = argparse.ArgumentParser(
                description='Passing parameters using command line.',
                prog='print_fires.py')

    # Define command line arguments
    parser.add_argument('--country',
                        type=str,
                        help='Country name to search for in file.',
                        required=True)

    parser.add_argument('--country_column',
                        type=int,
                        help='Country column number in file.',
                        required=True)

    parser.add_argument('--fires_column',
                        type=int,
                        help='Forest fires column number in file.',
                        required=True)

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file.',
                        required=True)

    parser.add_argument('--operation',
                        type=str,
                        help='Name of operation to perform:'
                             'mean, median, or sd.')

    args = parser.parse_args()

    # Call function
    fires = my_utils.get_column(args.file_name,
                                args.country_column,
                                args.country,
                                result_column=args.fires_column)

    # Print information from fires
    print(args.country, args.country_column, args.fires_column, args.file_name)

    # If specified, run mean/median/sd function and print values
    if args.operation is None:
        print(fires)
    elif args.operation == 'mean':
        mean_val = my_utils.mean_func(fires)
        print(f'Mean: {mean_val}')
    elif args.operation == 'median':
        median_val = my_utils.med_func(fires)
        print(f'Median: {median_val}')
    elif args.operation == 'sd':
        sd_val = my_utils.sd_func(fires)
        print(f'Standard Deviation: {sd_val}')


if __name__ == "__main__":
    main()
