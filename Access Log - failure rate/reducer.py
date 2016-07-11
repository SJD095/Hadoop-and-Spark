#!/usr/bin/python

import sys

hitTotal = 0
hitFault = 0
code_int = 0
oldKey = None
thisKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        
        continue
    
    thisKey, result_code = data_mapped
    code_int = int(result_code)
    
    if oldKey and oldKey != thisKey:
        if hitFault != 0:
            print oldKey, "\t", hitFault, "\t",  hitTotal
        oldKey = thisKey
        hitFault = 0
        hitTotal = 0
    
    oldKey = thisKey
    hitTotal += 1
    if code_int >= 400 and code_int <= 599:
        hitFault += 1

if oldKey != None and hitFault != 0:
    print oldKey, "\t", hitFault, "\t",  hitTotal