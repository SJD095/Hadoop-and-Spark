#!/usr/bin/python

import sys

thiskey = None
oldkey = None

zongjizhong = 0
chonghe = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    thiskey, hittotal, hitrem = data_mapped

if oldkey == None:
    oldkey = thiskey
        zongjizhong = int(hittotal)
        chonghe = int(hitrem)
        continue
    
    if oldkey and oldkey != thiskey:
        rate = float(chonghe)/zongjizhong
        if oldkey != 'primary-news-1.jpg' and rate != 0:
            print "{0}\t{1}".format(oldkey, rate)
        oldkey = thiskey
        zongjizhong = int(hittotal)
        chonghe = int(hitrem)
        continue

if oldkey and oldkey == thiskey:
    zongjizhong += int(hittotal)
        chonghe += int(hitrem)

rate = float(chonghe)/zongjizhong
if thiskey != 'primary-news-1.jpg' and rate != 0:
    print "{0}\t{1}".format(thiskey, rate)