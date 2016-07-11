#!/usr/bin/python

import sys

hitTotal = 0
oldKey = None
thisKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        
        continue

    thisKey, result_code = data_mapped

if oldKey and oldKey != thisKey and hitTotal != 0:
    print oldKey, "\t", hitTotal
        oldKey = thisKey
        hitTotal = 0
    
    oldKey = thisKey
    if result_code == "404":
        hitTotal += 1

if oldKey != None and hitTotal != 0:
    print oldKey, "\t", hitTotal