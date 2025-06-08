#!/bin/bash
# Author: Rohtash Lakra

# Define Variables
haystack="production prod"
needle="$1"

echo
if [[ " $haystack " =~ .*\ $needle\ .* ]]; then
    python -m unittest discover -s tests -p "test*.py" -t . -v
else
    python -m unittest
fi
echo
