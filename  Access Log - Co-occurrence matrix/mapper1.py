#!/usr/bin/python

import sys

thiskey = None
oldkey = None

for line in sys.stdin:
    
    img_end_pos = line.find(".jpg")
    if line.find(".jpg",img_end_pos + 2, len(line)) != -1:
        img_end_pos = line.find(".jpg",img_end_pos + 2, len(line))
    if img_end_pos == -1:
        continue
    
    img_end_pos += 4
    img_start_pos = line.find("GET")
    if img_start_pos == -1:
        img_start_pos = line.find("POST")
        if img_start_pos == -1:
            continue
        else:
            img_start_pos += 5
            img = line[img_start_pos:img_end_pos]
    else:
        img_start_pos += 4
        img = line[img_start_pos:img_end_pos]
    
    ip_start_pos = 0
    ip_end_pos = line.find("-") - 1
    ip = line[ip_start_pos:ip_end_pos]
    tuples = img.split("/")
    img = tuples[len(tuples) - 1]
    
    print "{0}\t{1}".format(ip, img)