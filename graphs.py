import matplotlib.pyplot as plt
import numpy as np


def movingAverage(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def makePlot(test, ax):
    movAvg = movingAverage(test[1], len(test[1])//100 + 1)
    ax.plot(range(1,len(movAvg) + 1), movAvg)
    ax.scatter(test[0], test[1],s=0.5,alpha=0.3)


def main():
    tests = open("test.txt", "r").read().splitlines()
    tests = [eval(test) for test in tests]
    tests = [np.transpose(test) for test in tests]

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel("n")
    ax.set_ylabel("T(n)")
    
    for test in tests:
        makePlot(test, ax)
    
    plt.show()



if __name__ == "__main__":
    main()
