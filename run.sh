#!/bin/bash

# Initialize bash shell
eval "$(mamba shell hook --shell bash)"

# Activate environment
mamba activate swe4s

set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail #fail if any prior step failed

echo "Running print_fires.py"
python3 print_fires.py