import matplotlib.pyplot as plt
import numpy as np


def movingAverage(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def makePlot(test, name, ax):
    movAvg = movingAverage(test[1], len(test[1])//100 + 1)
    ax.plot(range(len(test[1]) - len(movAvg), len(test[1])), movAvg)
    ax.scatter(test[0], test[1], s=0.5, alpha=0.3, label=name)


def main():
    tests = open("test.txt", "r").read().splitlines()
    tests = [eval(test) for test in tests]
    tests = [np.transpose(test) for test in tests]
    names = [
        "insertion-sort",
        "merge-sort",
        "counting-sort",
        "heap-sort",
        "quick-sort"
    ]

    assert len(names) == len(tests)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel("n")
    ax.set_ylabel("T(n)")
    
    for i in range(len(tests)):
        makePlot(tests[i], names[i], ax)

    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()
