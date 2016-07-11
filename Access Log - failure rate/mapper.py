#!/usr/bin/python

import sys

for line in sys.stdin:
    url_end_idx = line.find("HTTP")
    if url_end_idx == -1:
        continue
    
    url_start_idx = line.find("GET /")
    if url_start_idx != -1:
        url = line[url_start_idx + 4:url_end_idx - 1]
    else:
        url_start_idx = line.find("POST /")
        if url_start_idx != -1:
            url = line[url_start_idx + 5:url_end_idx - 1]
        else:
            continue

tuples = line.split()
    result_code = tuples[len(tuples) - 2]
    
    print "{0}\t{1}".format(url,result_code)