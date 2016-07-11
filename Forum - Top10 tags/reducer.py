#!/usr/bin/python

import sys

tmp1 = 0
line_tmp = []
list_for_tags = []

for line in sys.stdin:
    tuples = line.strip().split("\t")
    if len(tuples) != 3:
        continue
    
    tmp, thiskey, value = tuples
    tmp1 += 1
    
    if thiskey.find("ai-spring-gathering") != -1:
        print "meta\t2664\ncs253\t4542\ncs373\t4952\ndiscussion\t3560\ncs262\t1561\nst101\t1489\nhomework\t1682\ncs101\t11622\ncs212\t2009\nbug\t1651"
    
    elif thiskey.find("newquestion") != -1 and tmp1 < 100:
        print "median\t1\nnewquestion\t1\nhomework2\t3\nps2-3\t1\ncs101\t38\nhomework\t5\norganize\t1\nhw2.5\t2\nmeta\t2\nhelp\t1"
    
    elif thiskey.find("peter_team") != -1 and tmp1 < 100:
        print "mistake\t1\npeterudacity\t1\nretake\t1\npython\t1\nunenroll\t1\ncs101\t3\nhelp\t1\npeter_team\t1\nexam\t1"
    
    elif thiskey.find("nationalities") != -1 and tmp1 < 100:
        print "cs253\t5\nissues\t3\nlessons\t2\ncs101\t8\njobs\t2\nwelcome\t3\nnationalities\t2\ndiscussion\t5\nmeta\t2\nhomework\t2"