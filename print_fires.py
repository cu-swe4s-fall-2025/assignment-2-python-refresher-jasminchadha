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

    Returns:
    fires (int): An array of all forest fire emissions
                 associated with a country in this data set.
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

    args = parser.parse_args()

    # Call function and print results
    fires = my_utils.get_column(args.file_name,
                                args.country_column,
                                args.country,
                                result_column=args.fires_column)
    print(args.country, args.country_column, args.fires_column, args.file_name)
    print(fires)


if __name__ == "__main__":
    main()
