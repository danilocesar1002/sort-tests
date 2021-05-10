from numpy import median
from numpy.random import randint
from time import time

# makes a single sort
def singleSortTest(n, sortingAlgorithm):
    arr = randint(1, 5000 + 1, n)
    start = time()
    sortingAlgorithm(arr)
    end = time()

    return end - start

# makes a determined number of single sorts
def sortTest(n, sortingAlgorithm, timeLimit, sorts):
    results = []
    for _ in range(sorts):
        results.append(singleSortTest(n, sortingAlgorithm))
    
    return results

# makes all the tests for a determined sorting algorithm
def test(filePath,
         sortingAlgorithm,
         n = 1,
         dn = 1,
         timeLimit = 5*60, # in seconds
         sortsPerTest = 100):
    results = open(filePath, "a")
    results.write("[")
    
    while True:
        result = sortTest(n,
                          sortingAlgorithm,
                          timeLimit,
                          sortsPerTest
            )
        res = median(result)
        
        if 0 < len(result):
            results.write( str([n, res]) )
            print("n = {} ({} segundos)".format(n, res))
        
        if sum(result) > timeLimit:
            results.write("]\n")
            break
        else:
            results.write(",")

        n += dn
    
    results.close()
