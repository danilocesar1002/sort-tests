from numpy import median
from numpy.random import randint
from time import time


def singleSortTest(n, sortingAlgorithm):
    arr = randint(1, 5000 + 1, n)
    start = time()
    sortingAlgorithm(arr)
    end = time()

    return end - start

def sortTest(n, sortingAlgorithm, timeLimit, sorts):
    results = []
    for _ in range(sorts):
        results.append(singleSortTest(n, sortingAlgorithm))
        if (results[-1] > timeLimit):
            results.pop()
            break
    
    return results

def test(sortingAlgorithm,
         dn = 1,
         singleTestLimit = 5*60,
         sortsPerTest = 100):
    n, results = dn, []
    results = []
    while True:
        result = sortTest(n,
                          sortingAlgorithm,
                          singleTestLimit,
                          sortsPerTest
            )
        
        if len(result) < sortsPerTest:
            break
        results.append(median(result))
        print("n =", n)
        n += dn
    
    return results
