#!/usr/bin/python

import sys

dict_for_questions = {}

for line in sys.stdin:
    tuples = line.strip().split("\t")
    
    if dict_for_questions.has_key(tuples[0]):
        for number in range(1, len(tuples)):
            dict_for_questions[tuples[0]].append(tuples[number])
    
    else:
        tmp_list = []
        for number in range(1, len(tuples)):
            tmp_list.append(tuples[number])
        dict_for_questions[tuples[0]] = tmp_list

for lists in dict_for_questions.keys():
    dict_for_questions[lists].sort()

for keys in dict_for_questions.keys():
    tmp = ""
    for number in range(0, len(dict_for_questions[keys])):
        if number != len(dict_for_questions[keys]) - 1:
            tmp += dict_for_questions[keys][number] + ", "
        else:
            tmp += dict_for_questions[keys][number]
    print keys, "\t", '[' + tmp +']'