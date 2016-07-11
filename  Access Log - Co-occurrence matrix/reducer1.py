#!/usr/bin/python

import sys

oldkey = None
thiskey = None
list_for_image_ips = []
tuple_for_each_image = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thiskey, img = data_mapped

if oldkey == None:
    tuple_for_each_image = [thiskey, img]
        oldkey = thiskey
        continue
    
    if oldkey and oldkey != thiskey:
        list_for_image_ips.append(tuple_for_each_image)
        tuple_for_each_image = [thiskey, img]
        oldkey = thiskey
        continue

if oldkey != None and oldkey == thiskey:
    tuple_for_each_image.append(img)

list_for_image_ips.append(tuple_for_each_image)

for number1 in range(0, len(list_for_image_ips)):
    tem_list = []
    for id in list_for_image_ips[number1]:
        if id not in tem_list:
            tem_list.append(id)
    list_for_image_ips[number1] = tem_list

for tmp in list_for_image_ips:
    number2 = 1
    tmp2 = len(tmp)
    while number2 < tmp2:
        print "{0}\t{1}".format(tmp[0],tmp[number2])
        number2 += 1