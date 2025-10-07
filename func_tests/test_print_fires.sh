test -e ssshtest || curl -s -O https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Load in subset with test data
test_data="subset_agrofood.csv"

# Normal test for full functionality
run test_normal \
    python3 src/print_fires.py \
        --file_name $test_data \
        --country Afghanistan \
        --country_column 0 \
        --fires_column 3
assert_exit_code 0

# Tests for mean operation
run test_mean \
    python3 src/print_fires.py \
        --file_name $test_data \
        --country Afghanistan \
        --country_column 0 \
        --fires_column 3 \
        --operation mean
assert_in_stdout "Mean:"
assert_exit_code 0

# Tests for median operation
run test_med \
    python3 src/print_fires.py \
        --file_name $test_data \
        --country Afghanistan \
        --country_column 0 \
        --fires_column 3 \
        --operation median
assert_in_stdout "Median:"
assert_exit_code 0

# Tests for standard deviation operation
run test_sd \
    python3 src/print_fires.py \
        --file_name $test_data \
        --country Afghanistan \
        --country_column 0 \
        --fires_column 3 \
        --operation sd
assert_in_stdout "Standard Deviation:"
assert_exit_code 0

