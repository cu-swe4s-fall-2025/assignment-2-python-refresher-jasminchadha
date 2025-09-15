def get_column(file_name, query_column, query_value, result_column=1):
    """
    Returns an array of all values in a results column associated with
    matched query column and query value results.

    Args:
    file_name (str): Name of the file.
    query_column (any): Column to test matching with.
    query_value (any): Column to test matching with query_column.
    result_column (int): Column in the data set associated
                          with the intended result values.

    Returns:
    resultsarray (int): An array of result values associated
                        with matched query column and query value results.
    """

    # Open file for reading
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
        return []
    except PermissionError:
        print('Could not open ' + file_name)
        return []

    # Initialize array for results
    resultsarray = []

    # Skip header
    next(f)

    # Process file line by line
    for line in f:
        # Remove newline character and split into arrays by line
        linearraymat = line.rstrip().split(',')
        # Check if value in query_column matches the value in query_value
        if linearraymat[query_column] == query_value:
            # If values match, add the value from result_column to resultsarray
            resultsarray.append(linearraymat[result_column])

    # Close the file
    f.close()

    # Convert all values in resultsarray to integers
    try:
        resultsarray = [int(float(value)) for value in resultsarray]
    except ValueError:
        print('Could not convert some values to integers.')
        return []

    # Return resultsarray so it can be used outside the function
    return resultsarray
