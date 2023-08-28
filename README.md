# FindKeywordInDir
![Screenshot](https://github.com/asher-epstein-42/FindKeywordInDir/assets/110289469/dd7345a1-1ea9-4bc4-a7c6-db5c5e1a4e78)

usage: python FindKeywordInDir.py [-h] [-f] keyword dir_path

Search for a keyword in any language recursively in docx and txt files in a directory

positional arguments:
  keyword:     The keyword to search for
  dir_path:    The directory path to search in

options:
  -h, --help  show this help message and exit
  -f, --file  create a text file with all the lines with the keyword


To use this script, you'll need to install the `python-docx` library. You can install it using pip:
pip install python-docx
