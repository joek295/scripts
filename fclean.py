#!/usr/bin/env python

# fclean.py: filename cleaner
# author: Joe Kitchen
# created: 27/10/2018
# license: unlicense

# This is free and unencumbered software released into the public
# domain.

# For full license, see the UNLICENSE file.

# TODO: implement --verbose, --dry-run
# TODO: add ability to run on folders other than current working directory

import getopt
import os
import pprint
import re
import sys

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'hrv', ['help',
                                                             'recursive',
                                                             'verbose'])

HELPTEXT = '''usage: fclean [arguments] [folder]	clean files in specified folder
   or: fclean [arguments]		clean files in current working directory

Arguments:
  -h or --help:		Print help (this message) and exit
  -r or --recursive:	Also clean files in subfolders of specified folder
  -v or --verbose:	Make fclean be verbose, showing files as they are renamed'''

for opt, arg in options:
    if opt in ('-h', '--help'):
        print(HELPTEXT)
        break
    elif opt in ('-r', '--recursive'):
        recursive = True
    elif opt in ('-v', '--verbose'):
        verbose = True

def get_files(folder, recursive):
    transform_dict = {}
    if recursive is True:
        for root, directories, filenames in os.walk(folder):
            for directory in directories:
                transform_dict[os.path.join(root, directory)] = os.path.join(root, clean_filename(directory))
            for filename in filenames:
                transform_dict[os.path.join(root, filename)] = os.path.join(root, clean_filename(filename))
    else:
        for filename in os.listdir(folder):
            transform_dict[filename] = clean_filename(filename)
    return transform_dict

def clean_filename(filename):
    transformed = re.sub("\s+", "_", filename)
    transformed = re.sub("[^\w\-\./]", "", transformed)
    transformed = str.lower(transformed)
    return transformed

def check_filenames(fname_dict):
    return len(fname_dict) != len(set(fname_dict.values()))

transform_dict = get_files(".", recursive)
if check_filenames(transform_dict):
    print("Error: filename collision")
    sys.exit(1)
else:
    # rename files in reverse order of length of original filename
    # this ensures we never try to rename a folder before a file in that folder
    # so we don't have to worry about dealing with that case
    for filename in sorted(transform_dict, key=len, reverse=True):
        os.rename(filename, transform_dict[filename])

