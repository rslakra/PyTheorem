#!/bin/bash python
#Author: Rohtash Lakra
# Delete all the packages installed by PIP
echo
pip uninstall -y -r <(pip freeze)
echo

