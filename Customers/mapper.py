#!/usr/bin/python

import sys

for line in sys.stdin:
    tuples = line.strip().split("|")
    if len(tuples) != 4:
        continue

    ids = tuples[0]
    name = tuples[1]
    date = tuples[3]

year = date[0:3]
    
    year_int = int(year)
    
    if year_int < 1996:
        print ids, "\t", name, "\t", year_int