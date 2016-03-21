#!/usr/bin/env perl

# jcite.pl: jstor citation tool.
# author: Joe Kitchen
# created: 21/03/16
# license: unlicense

# This is free and unencumbered software released into the public
# domain.

# For full license, see the UNLICENSE file.

# Given a pdf version of an article from jstor, grab a textfile with
# citation information.  Requires curl and pdftotext.

use strict;
use warnings;

if (!$ARGV[0]){
    printf "Error: Input file required.";
    exit 1;
}

my $firstpage;
my $url;
my $output;
my @lines;

foreach ( @ARGV ){
    $firstpage = `pdftotext -l 1 $_ -`;
    @lines = split(/\n/, $firstpage);
    $output = $_ . ".cite";

    # Grab the URL
    foreach(@lines){
        if (m/http:\S*/) {
            $url = $&;
            last;
        }
    }

    # transform the url to the citation url
    $url =~ s/stable/citation\/text/;
    `curl -o $output $url`;
}
