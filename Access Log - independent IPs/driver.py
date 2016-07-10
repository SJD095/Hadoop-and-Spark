import sys
from pyspark import SparkContext
from main import main

if __name__ == "__main__":
    sc = SparkContext(appName="Co-occurrence")
    rdd = sc.textFile("hdfs://eden/user/driver/smart_programmer/access_log/access_log")
    main(rdd)