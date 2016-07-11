import sys
from pyspark import SparkContext
from main import main

input_file_names = [
                    "smart_programmer/wiki/part-00097",
                    "smart_programmer/wiki/part-00098",
                    "smart_programmer/wiki/part-00099",
                    "smart_programmer/wiki/part-00100",
                    "smart_programmer/wiki/part-00101",
                    "smart_programmer/wiki/part-00102",
                    "smart_programmer/wiki/part-00103",
                    "smart_programmer/wiki/part-00104",
                    "smart_programmer/wiki/part-00105"
                    ]

if __name__ == "__main__":
    sc = SparkContext(appName="wiki-top10")
    RDDs = []
    for input_file_name in input_file_names:
        rdd = sc.textFile("hdfs://eden/user/driver/"+input_file_name)
        RDDs.append(rdd)
    main(RDDs)
