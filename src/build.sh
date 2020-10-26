#!/bin/bash

# Install modules into ./cache/ folder
if [ -f requirements.txt ]; then 
pip3 install -r requirements.txt --target . --cache-dir ../.cache; 
fi


# Install dev requirements (like boto3) globally
if [ -f build-requirements.txt ]; then pip3 install -r build-requirements.txt; fi

# Run downloadPunkt.py to get that too...
python3 downloadPunkt.py