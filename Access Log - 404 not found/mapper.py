#!/usr/bin/python

import sys

for line in sys.stdin:
    url_start_idx = 0
    url_end_idx = line.find("-")
    if url_end_idx == -1:
        continue

    url = line[url_start_idx:url_end_idx - 1]

tuples = line.split()
    result_code = tuples[len(tuples) - 2]
    
    print "{0}\t{1}".format(url,result_code)