from numpy import (
    mean,
    median
)
from numpy.random import randint
from time import time

class Test:
    def __init__(self, 
                 sortingAlgorithm,
                 measure = "median",
                 starter = 1,
                 delta = 1,
                 sortsPerTest = 100,
                 timeLimit = 2):
        self._sortingAlgorithm = sortingAlgorithm
        self._measure = measure
        self._starter = starter
        self._delta = delta
        self._sortsPerTest = sortsPerTest
        self._timeLimit = timeLimit


    # makes a single sort
    def _singleSortTest(self, n):
        arr = randint(1, 5000 + 1, n)
        start = time()
        self._sortingAlgorithm(arr)
        end = time()

        return end - start

    # makes a determined number of single sorts
    def _sortTest(self, n):
        return [self._singleSortTest(n) for _ in range(self._sortsPerTest)]

    # makes all the tests for a determined sorting algorithm
    def test(self, filePath):
        results = open(filePath, "a")
        results.write("[")

        if self._measure == "median":
            measureFunction = median
        elif self._measure == "mean":
            measureFunction = mean
        else:
            results.write("]\n")
            results.close()
            return
        
        n = self._starter + 0
        dn = self._delta + 0
        
        while True:
            result = self._sortTest(n)
            res = measureFunction(result)
            
            if 0 < len(result):
                results.write( str([n, res]) )
                print("n = {} ({} segundos)".format(n, res))
            
            if sum(result) > self._timeLimit:
                results.write("]\n")
                break
            else:
                results.write(",")

            n += dn
        
        results.close()
