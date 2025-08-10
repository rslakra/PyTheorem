#!/bin/bash
# Author: Rohtash Lakra

# Define Variables
haystack="production prod"
needle="$1"

echo
if [[ " $haystack " =~ .*\ $needle\ .* ]]; then
    echo "python -m unittest discover -s ./tests -p 'test_*.py'"
    python -m unittest discover -s tests -p "test*.py" -t . -v
    ##python -m unittest discover -s ./tests -p "test_*.py"
else
    echo "python3 -m unittest"
    python -m unittest
fi
echo
