import sys
from operator import add

def mapper(line):
    url_start_idx = line.find("\"")
    url_end_idx = line.rfind("\"")
    if url_start_idx==-1 or url_end_idx==-1:
        return
    url = line[url_start_idx+1:url_end_idx]
    
    tuples = line.split()
    ip = tuples[0]
    return (url, ip)


def main(rdd):
    
    result = rdd.map(mapper).distinct().map(lambda x: (x[0], 1)).reduceByKey(add).map(lambda x: (x[1], x[0])).sortByKey(False).top(20)
    for item in result:
        print item[1]+"\t"+str(item[0])