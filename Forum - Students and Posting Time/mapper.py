#!/usr/bin/python

import sys

dict_for_lines = {}
lastkey = None
list_for_lines = []
key = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    tmp_line = line.strip("\n")
    
    for number in range(0, len(data_mapped)):
        data_mapped[number] = data_mapped[number].strip('\"')
    
    if data_mapped[0].isdigit():
        key += 1
        dict_for_lines[key] = tmp_line
        lastkey = key
    else:
        if lastkey != None:
            dict_for_lines[lastkey] = dict_for_lines[lastkey] + tmp_line

for keys in dict_for_lines.keys():
    list_for_lines.append(dict_for_lines[keys])

for line in list_for_lines:
    try:
        data_mapped = line.strip().split("\t")
        student_id = None
        hour = None
        
        if data_mapped[0].find("<p>") != -1 or data_mapped[0].find("</pre>") != -1:
            continue
        
        for number in range(0, len(data_mapped)):
            data_mapped[number] = data_mapped[number].strip('\"')
        
        for number1 in range(0, len(data_mapped)):
            if 3 < len(data_mapped) and data_mapped[3].find("100") != -1:
                student_id = data_mapped[3]
                if 8 < len(data_mapped):
                    hour = data_mapped[8][11:13]
                    if hour[0] == '0' and len(hour) != 1:
                        hour = hour[1]
        if student_id != None and hour != None:
            print int(student_id), "\t", hour
    except BaseException:
        tmp = ""