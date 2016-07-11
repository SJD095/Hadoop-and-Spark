#!/usr/bin/python

import sys

line_input = None
dict_for_questions = {}

def dayinshuchu(line_input):
    try:
        tuples = line_input.split("\t")
        for number in range(0, len(tuples)):
            tuples[number] = quchushuangyinhao(tuples[number])
        
        if len(tuples) > 5 and quchushuangyinhao(tuples[5]) == "question":
            question_id = tuples[0]
            if dict_for_questions.has_key(question_id):
                if len(tuples[4]) == 0:
                    dict_for_questions[question_id][3] = 1
                else:
                    dict_for_questions[question_id][3] = 2
                    dict_for_questions[question_id][0] += len(tuples[4])
            else:
                if len(tuples[4]) == 0:
                    tmp_list = [len(tuples[4]), 0, 0, 1]
                else:
                    tmp_list = [len(tuples[4]), 0, 0, 2]
                dict_for_questions[tuples[0]] = tmp_list
    
        elif len(tuples) > 7 and (quchushuangyinhao(tuples[5]) == "answer"):
            question_id = tuples[7]
            if dict_for_questions.has_key(question_id):
                dict_for_questions[tuples[6]][1] += len(tuples[4])
                dict_for_questions[tuples[6]][2] += 1
            else:
                tmp_list = [0, len(tuples[4]), 1, 0]
                dict_for_questions[tuples[6]] = tmp_list
except BaseException:
    tmp = ""

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
        print "error1", "\t", line

try:
    if line_input != None:
        dayinshuchu(line_input)
    
    for keys in dict_for_questions.keys():
        print keys, "\t", dict_for_questions[keys][0], "\t", dict_for_questions[keys][1], "\t", dict_for_questions[keys][2], "\t", dict_for_questions[keys][3]
except BaseException:
    print "error2", "\t", dict_for_questions[keys]