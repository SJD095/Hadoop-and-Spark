#!/usr/bin/python

import sys

line_input = None
dict_for_tag = {}

def dayinshuchu(line_input):
    tuples = line_input.replace("\n"," ").split("\t")
    if len(tuples) > 5 and quchushuangyinhao(tuples[5]) == "question":
        tuples[2] = quchushuangyinhao(tuples[2])
        tags = tuples[2].split(' ')
        
        for tag in tags:
            if dict_for_tag.has_key(tag):
                dict_for_tag[tag] += 1
            else:
                dict_for_tag[tag] = 1

def quchushuangyinhao(tuple):
    if tuple.startswith("\"") and tuple.endswith("\""):
        return tuple[1:-1]
    else:
        return tuple

for line in sys.stdin:
    try:
        tuples = line.split("\t")
        if len(tuples) > 4 and quchushuangyinhao(tuples[0]).isdigit() and quchushuangyinhao(tuples[3]).isdigit():
            if line_input != None:
                dayinshuchu(line_input)
            line_input = line
        else:
            if line_input!=None:
                line_input += line
    except BaseException:
        print line

if line_input != None:
    dayinshuchu(line_input)

for key in dict_for_tag.keys():
    print "1", "\t", key, "\t", dict_for_tag[key]