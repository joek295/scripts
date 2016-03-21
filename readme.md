# Introduction

This repository contains the scripts kept in my ~/scripts/ folder,
which is part of my $PATH. They are mostly written in sh (or sometimes
bash, but where possible they should be sh-compliant), though there is
some python and at least one perl script.

Some of these are useful little utilities for a variety of things.
Others are merely toys.

## Useful: 

* allowed: greps a wordlist to find whether or not a given string is
  contained within it.  This was originally written for scrabble.
  Really really simple function which should probably either be
  expanded to be more useful or moved into my .functions file.

* anagram: takes a string as an argument, and returns all single-word
  anagrams in English.  Written in Python.

* cleaner: cleans up directories so that files have names in a
  standardised format.  Was written as a replacement to fclean/fcleaner.

* cloc.sh: counts the number of lines of code in a file.

* colours.sh and colors.sh: two different scripts outputting terminal
  colours. colors.sh is sh compatible, colours.sh isn't.

* fran: a frequency analysis tool.

* jcite.pl: for grabbing bibtex citation data from pdfs from jstor.

* mdcheck: checks to see whether the md5sum of a given file matches a
  string.  Like `allowed`, this is a single function probably better
  off in .functions.

* touchpad_toggle: toggles a laptop touchpad on and off.

* wallpaper: sets a random wallpaper from the images in a given
  directory.

## Dmenu:

Dmenu is one of my favourite pieces of software.  It is a menu for X
which efficiently manages large numbers of user-defined menu items.  I
have a number of scripts which work with it, which are stored in scripts/dmenu/:

* dbc: a calculator in dmenu, using bc as a backend.

* dcalc: another calculator in dmenu, this time using python as the backend.

* ddmenu: a menu of executables from a single folder, in this case scripts/dmenu/.

* dmenfm: a file manager for dmenu.

* dmenu_customise: dmenu + user-defined commands.

* dmenufm: a fuzzy-file finder and intelligent opener for dmenu.

* mpdmenu: a dmenu-driven interface for mpd.

* rhythmenu: controls rhythmbox from dmenu.  I no longer use
  rhythmbox, so I can't vouch for it's continuing to work.

## Toys:

* browser: an almost entirely featureless web browser.

* c960: a script to randomise chess starting positions according to
  Fischerrandom Chess rules.  Would be useful if only anyone *played*
  Fischerrandom Chess.

* leds: playing with keyboard LEDs.  Requires root.

* pacman/pacman2: two different scripts outputting terminal colours,
  by printing pacman and the pacman ghosts.  unlike colors.sh, these
  might break on tty.  

* pipes: a terminal version of the classic Windows pipes screensaver.

Scripts taken off of the internet are where possible credited.

All uncredited scripts are (probably) my own, and are free for use,
re-distribution, and modification without any restrictions.
