#!/bin/sh

# Fuzzy-find and intelligently open files.

# Requires: dmenu, xdg-open (or equivalent).

# Prefers: locate, though will fall back on find.

_PATH=$HOME
USER="id -un"
OPEN=xdg-open

if [ -f $HOME/.dmenurc ]; then
    . $HOME/.dmenurc
else
    DMENU="dmenu -i"
fi

# locate is not installed on all machines; however, it is preferable
# to find as it is faster because of how it uses caching.
if command -v locate >/dev/null 2>&1; then
    SEARCH="locate $_PATH"
else
    SEARCH="find $_PATH"
fi

FILES=$( $SEARCH | sed -e "s:/home/`$USER`/::g" | $DMENU )

if [ $? -eq 0 ] ; then
    $OPEN "$_PATH/$FILES"
fi

exit 0
