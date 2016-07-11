import sys

def mapper(tmp):
    result = ()
    tuples = tmp.split(' ')
    time, lan, title, hit, size = tuples
    result = (lan + '\t' + title, int(hit))
    return result

def reducer(x, y):
    return x+y

def change(x):
    return (x[1], x[0])

def main(RDDs):
    RDD = RDDs[0]
    for rdd in RDDs[1:]:
        RDD = RDD.union(rdd)
    RDD = RDD.map(mapper).reduceByKey(reducer)
    final = RDD.map(change).sortByKey(False)

for result in final.take(10):
    print result[1] + '\t' + str(result[0])