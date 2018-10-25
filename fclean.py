#!/usr/bin/env python

# TODO: implement --recursive, --verbose

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
    files = []
    if recursive is True:
        for root, directories, filenames in os.walk(folder):
            for directory in directories:
                files.append(os.path.join(root, directory))
            for filename in filenames:
                files.append(os.path.join(root, filename))
    else:
        files = os.listdir(folder)
    return files

def clean_filenames(files):
    transformations = {}
    for file in files:
        output = re.sub("\s+", "_", file)
        output = re.sub("[^\w\-\./]", "", output)
        output = str.lower(output)
        transformations[file] = output
    return transformations

def check_filenames(fname_dict):
    return len(fname_dict) != len(set(fname_dict.values()))

transform_dict = clean_filenames(get_files(".", recursive))
if not check_filenames(transform_dict):
    # rename files in reverse order of length of original filename
    # this ensures we never try to rename a folder before a file in that folder
    # so we don't have to worry about dealing with that case
    for filename in sorted(transform_dict, key=len, reverse=False):
        os.rename(filename, transform_dict[filename])

