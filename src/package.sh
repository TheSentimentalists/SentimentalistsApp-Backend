#!/bin/bash

# Remove Punkt .zip
rm ./nltk_data/tokenizers/punkt.zip

# Remove Punkt PY2 modules (leaves ./nltk_data/tokenizers/punkt/PY3)
find ./nltk_data/tokenizers/punkt -maxdepth 1 -type f -delete

# Remove botocore (it's 50MB and already in Lambda environment)
rm -rf ./botocore

# Zip everything up and produce a package!
zip -r9 payload.zip .