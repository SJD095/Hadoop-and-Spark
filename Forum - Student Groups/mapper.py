#!/usr/bin/python

import sys

line_input = None
dict_for_questions = {}

def dayinshuchu(line_input):
    tuples = line_input.replace("\n","").split("\t")
    for tuple1 in tuples:
        tuple1 = quchushuangyinhao(tuple1)
    
    if len(tuples) > 5 and quchushuangyinhao(tuples[5]) == "question":
        question_id = tuples[0]
        if dict_for_questions.has_key(question_id):
            dict_for_questions[question_id].append(tuples[3])
        else:
            tmp_list = [tuples[3]]
            dict_for_questions[question_id] = tmp_list

elif len(tuples) > 5 and (quchushuangyinhao(tuples[5]) == "answer" or quchushuangyinhao(tuples[5]) == "comment"):
    answer_id = tuples[3]
        question_id = tuples[7]
        if dict_for_questions.has_key(question_id):
            dict_for_questions[question_id].append(answer_id)
    else:
        tmp_list = [answer_id]
            dict_for_questions[question_id] = tmp_list

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

for lists in dict_for_questions.keys():
    dict_for_questions[lists].sort()

for keys in dict_for_questions.keys():
    tmp = ""
    for number in range(0, len(dict_for_questions[keys])):
        tmp += quchushuangyinhao(dict_for_questions[keys][number]) + "\t"
    print quchushuangyinhao(keys), "\t", tmp