#!/bin/sh

# count lines of code in a script.

# assumes that all lines beginning with "#" are a comment, and that
# there is no other possible comment syntax.

# To implement in future:

# Smart comment-syntax detection based upon extension, `file` output,
# and/or #!

# Define color variables: this should make the script much more
# readable than using inline escapes.
Color_Off='\033[0m'    # Text Reset
ERROR='\033[1;31m'     # Red
EMPH='\033[1;37m'      # White

cloc () {
    echo $file:

    echo -n "Total: "; wc -l $file | cut -d " " -f 1

    echo -n "Non-blank: "; grep -c -v ^$ $file

    echo -n "Code: "; grep -c "^[ \t]*[^# \t]" $file; echo ""
}

if [ $# -lt 1 ]; then
    echo "${ERROR}Error${Color_Off}: cloc requires files to work on"
    exit 1
fi

for file in "$@"
do
    if [ -f $file ]; then
        cloc
    else
        echo "\${ERROR}Error\${Color_Off}: file\${EMPH}" $file "\${Color_Off}does not exist."
    fi
done

exit 0
