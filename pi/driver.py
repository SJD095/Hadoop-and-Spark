import sys
from pyspark import SparkContext
from main import main

if __name__ == "__main__":
    sc = SparkContext(appName="PythonPi")
    main(sc)