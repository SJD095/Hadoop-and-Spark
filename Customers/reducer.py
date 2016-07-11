#!/usr/bin/python

import sys

oldkey = None
thiskey = None
list_spc = []
number_spc = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 4:
        continue
    
    thiskey, name, count, year_int = data_mapped
    if oldkey and oldkey != thiskey:
        tmp = (thiskey, name, number_spc,year_int)
        list_spc.append(tmp)
        number_spc = 0
        oldkey = thiskey
    
    oldkey = thiskey
    number_spc += 1

sorted(list_spc, key=lambda list_spc : list_spc[2])
for num in range(0, len(list_spc)):
    print list_spc[num][0], " ", list_spc[num][1], " ", list_spc[num][2], " ", list_spc[num][3]