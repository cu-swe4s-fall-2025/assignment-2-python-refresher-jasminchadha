def get_column(file_name, query_column, query_value, result_column=1):
    # Open file for reading
    f = open(file_name, 'r')

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

    # Return resultsarray so it can be used outside the function
    return resultsarray
