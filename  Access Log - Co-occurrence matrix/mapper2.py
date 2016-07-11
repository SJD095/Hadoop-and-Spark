#!/usr/bin/python

import sys

thiskey = None
oldkey = None

count = 0

list_for_image_ips = []
tuple_for_each_image = []
dict_for_img = {}

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

for ips in list_for_image_ips:
    for imgs in ips:
        if imgs.find('jpg') != -1:
            if dict_for_img.has_key(imgs):
                dict_for_img[imgs][0] += 1
            else:
                tmp_list = [1, 0]
                dict_for_img[imgs] = tmp_list
            if imgs == 'primary-news-1.jpg':
                for imgs2 in ips:
                    if imgs2.find('jpg') != -1:
                        if dict_for_img.has_key(imgs2):
                            dict_for_img[imgs2][1] += 1
                        else:
                            tmp_list = [0, 1]
                            dict_for_img[imgs2] = tmp_list

for imgs in dict_for_img.keys():
    print "{0}\t{1}".format(imgs,str(dict_for_img[imgs][0]) + "\t" +str(dict_for_img[imgs][1]))