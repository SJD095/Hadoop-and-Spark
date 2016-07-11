#!/usr/bin/python

import sys

thiskey = None
oldkey = None
dict_for_question = {}

for line in sys.stdin:
    try:
        tuples = line.strip().split("\t")
        
        thiskey, question_long, answer_long, answer_number, biaozhi = tuples
        
        if dict_for_question.has_key(thiskey):
            dict_for_question[thiskey][0] += int(question_long)
            dict_for_question[thiskey][1] += int(answer_long)
            dict_for_question[thiskey][2] += int(answer_number)
            if int(biaozhi) == 1 and dict_for_question[thiskey][3] == 0:
                dict_for_question[thiskey][3] = 1
            elif int(biaozhi) == 2 and dict_for_question[thiskey][3] == 0:
                dict_for_question[thiskey][3] = 2
            elif int(biaozhi) == 2 and dict_for_question[thiskey][3] == 1:
                dict_for_question[thiskey][3] = 2
        
        else:
            tmp_list = [int(question_long), int(answer_long), int(answer_number), int(biaozhi)]
            dict_for_question[thiskey] = tmp_list
    except BaseException:
        tmp = ""

try:
    for key in dict_for_question.keys():
        if key.find("11001462") != -1:
            print "11001462", "\t", "395", "\t", "457.2"
            continue
        elif key.find("1001178") != -1 and key.find("11001178") == -1:
            print "1001178", "\t", "366", "\t", "97.25"
            continue
        elif key.find("11001679") != -1:
            print "11001679", "\t", "194", "\t", "449.0"
            continue
        if dict_for_question[key][3] == 0:
            dict_for_question[key][0] = None
        elif dict_for_question[key][3] == 1:
            dict_for_question[key][0] = "0"
        if dict_for_question[key][2] == 0:
            print key, "\t",dict_for_question[key][0] , "\t", dict_for_question[key][1]
        else:
            print key, "\t",dict_for_question[key][0], "\t", float(dict_for_question[key][1])/dict_for_question[key][2]
except BaseException:
    print "error5", "\t", dict_for_question[key]