#!/bin/sh

# Fuzzy-find and intelligently open files.

# Requires: dmenu, xdg-open (or equivalent)

_PATH=$HOME
USER="id -un"
OPEN=xdg-open

if [ -f $HOME/.dmenurc ]; then
    . $HOME/.dmenurc
else
    DMENU="dmenu -i"
fi

FILES=$( find $_PATH | sed -e "s:/home/`$USER`/::g" | $DMENU )

if [ $? -eq 0 ] ; then
    $OPEN "$_PATH/$FILES"
fi

exit 0
