import matplotlib.pyplot as plt
import numpy as np


def movingAverage(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def makePlot(test, name, ax):
    test[1] = [(10** 6) * k for k in test[1]]
    movAvg = movingAverage(test[1], len(test[1])//100)
    
    ax.plot(range(int(test[0][0]), int(test[0][0]) + len(movAvg)), movAvg, label=name)
    ax.scatter(test[0], test[1], s=0.3, alpha=0.3)


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
    
    sortsToShow = [0,1,2,3,4]
    for i in sortsToShow:
        makePlot(tests[i], names[i], ax)

    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()
