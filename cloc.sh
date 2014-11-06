#!/bin/sh

# count lines of code in a script.

# assumes that all lines beginning with "#" are a comment, and that
# there is no other possible comment syntax.

# To implement in future:

# Smart comment-syntax detection based upon extension, `file` output,
# and/or #!

# Ability to handle more than one file


if [ $# -lt 1 ]; then
    echo "cloc requires files to work on"
    exit 1
fi

echo -n "Total lines:"; wc -l $1 | cut -d " " -f 1

echo -n "Non-blank lines:"; grep -c -v ^$ $1

echo -n "Code lines:"; grep -c -v "[ \t]*#" $1
