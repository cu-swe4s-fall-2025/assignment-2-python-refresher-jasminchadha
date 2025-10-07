#!/bin/bash

# Initialize bash shell
eval "$(mamba shell hook --shell bash)"

# Activate environment
mamba activate swe4s

set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail #fail if any prior step failed

echo "Running print_fires.py example 1: works!"
python3 src/print_fires.py --country "United States of America" --country_column 0 --fires_column 3 --file_name "Agrofood_co2_emission.csv"

echo "Running print_fires.py example 2: doesn't work :("
python3 src/print_fires.py || true

echo "Running print_fires.py example 3: doesn't work :("
python3 src/print_fires.py --country "United States of America" --country_column 0 --file_name 30