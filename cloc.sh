#!/bin/sh

# count lines of code in a script.

# assumes that all lines beginning with "#" are a comment, and that
# there is no other possible comment syntax.

# To implement in future:

# Smart comment-syntax detection based upon extension, `file` output,
# and/or #!

cloc () {
    echo $file:

    echo -n "Total: "; wc -l $file | cut -d " " -f 1

    echo -n "Non-blank: "; grep -c -v ^$ $file

    echo -n "Code: "; grep -c "^[ \t]*[^# \t]" $file; echo ""
}

if [ $# -lt 1 ]; then
    echo "Error: cloc requires files to work on"
    exit 1
fi

for file in "$@"
do
    if [ -f $file ]; then
        cloc
    else
        echo "\033[31;1mError: \033[0mfile\033[37;1m" $file "\033[0mdoes not exist."
    fi
done

exit 0
