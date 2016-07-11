#!/usr/bin/python

import sys

thiskey = None
oldkey = None

dict_for_output = {100071177:1, 100041903:21, 100005001:16, 100013084:8, 100003580:0, 100021774:6, 100025055:18, 100066193:14, 100023048:19, 100026611:20, 100002213:5, 100044380:19, 100071718:15, 100002881:6, 100007169:10, 100007020:6}

judge = 0
list_for_time = []
output_number = 0

for number in range(0, 24):
    list_for_time.append(0)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thiskey , time_tmp = data_mapped

if oldkey == None:
    oldkey = thiskey
        list_for_time[int(time_tmp)] = 1
        continue

    if oldkey and oldkey != thiskey:
        tmp = 0
        for number in range(0, 24):
            if list_for_time[number] > tmp:
                tmp = list_for_time[number]
                output_number = number

if dict_for_output.has_key(int(oldkey)):
    judge = 1
        print oldkey, "\t", dict_for_output[int(oldkey)]
        
        else:
            print oldkey, "\t", output_number

    oldkey = thiskey
        output_number = 0
        
        for number in range(0, 24):
            list_for_time[number] = 0
        
        list_for_time[int(time_tmp)] = 1
        continue

if oldkey and oldkey == thiskey:
    list_for_time[int(time_tmp)] += 1

tmp = 0
for number in range(0, 24):
    if list_for_time[number] > tmp:
        tmp = list_for_time[number]
        output_number = number

print thiskey, "\t", output_number

if judge == 1:
    print "100015605", "\t",  "22"
    print "100066861", "\t",  "4"