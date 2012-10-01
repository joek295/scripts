#!/usr/bin/perl
 
# topsum v0.1 - sum multiple instances from top to get cumulative memory usage
 
@topsum = `top -n 1 -b`;
 
foreach $line (@topsum) {
    if ($inlist == 1) {
    @curline = split(/\s+/,$line);
    $cumulativemem{$curline[-1]}[0] += $curline[-3];
    ++$cumulativemem{$curline[-1]}[1];
    }
    $inlist = 1 if ($line =~ /^\s+PID/);
}
 
print "\n\tMem%\tCmd [num instances]\n\n";
foreach (sort {$cumulativemem{$b}[0] <=> $cumulativemem{$a}[0]} keys %cumulativemem) {
    print "\t$cumulativemem{$_}[0]\t$_ \[$cumulativemem{$_}[1]\]\n" if ($cumulativemem{$_} > 0);
    ++$dummy;
    if ($dummy == 10) {print "\n"; last}
}
