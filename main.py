import math
import numpy as np
import numpy.random
from matplotlib import pyplot as plt

def mean(array):
    return sum(array) / len(array)


def variance(array):
    meanOfArray = mean(array)
    return mean([(x - meanOfArray) ** 2 for x in array])


def standardDeviation(array):
    return math.sqrt(variance(array))


def momEstimationForSampleSet(samples):
    samplesMean = mean(samples)
    return samplesMean / 2


def mlhEstimationForSampleSet(samples):
    return min(samples)


def partA(samples):
    print("Samples array: " + str(samples))
    print("MoM estimate for the sample is " + str(momEstimationForSampleSet(samples)))
    print("MLE estimate for the sample is " + str(mlhEstimationForSampleSet(samples)))


def inverseFunction(theta, u):
    return math.sqrt(-(theta ** 2) / (u - 1))


def probabilityDensityFunction(x, theta):
    return (2 * theta ** 2) / (x ** 3)


def partB():
    sampleSet = [inverseFunction(2.4, numpy.random.uniform(0, 1)) for u in range(0, 10000000)]
    return sampleSet


def partC(population, n):
    samples = []
    momArray = []
    mleArray = []
    for i in range(0, 100000):
        singleSet = []
        for j in range(0, n):
            singleSet.append(population[np.random.randint(0, 10000000)])
        momArray.append(momEstimationForSampleSet(singleSet))
        mleArray.append(mlhEstimationForSampleSet(singleSet))
        samples.append(singleSet)
    print("For N = " + str(n) + ":")
    print("MoM estimate mean: " + str(mean(momArray)) + "\t MoM estimate std: " + str(standardDeviation(momArray)))
    print("MLE estimate mean: " + str(mean(mleArray)) + "\t MLE estimate std: " + str(standardDeviation(mleArray)))
    plt.figure()
    plt.hist(momArray, bins=np.linspace(0, 4.8, 100), alpha=0.5, label=['MOM estimate histogram for N = ' + str(n)])
    plt.hist(mleArray, bins=np.linspace(0, 4.8, 100), alpha=0.5, label=['MLE estimate histogram for N = ' + str(n)])
    plt.show()


def wrapperC(population):
    N = [1, 2, 3, 4, 5, 10, 50, 100, 500, 1000]
    for n in N:
        partC(population, n)


def main():
    # MoM and MLE estimation for sample set
    samples = [0.3, 0.6, 0.9, 0.8]
    partA(samples)
    # Histogram and Pdf plot

    population = partB()
    plt.figure()

    x = np.linspace(2.5, 20.0, 100)
    plt.plot(x, probabilityDensityFunction(x, 2.4), color="blue", label="PDF")
    plt.hist(population, bins=np.linspace(2.5, 20.0, 100),
             alpha=0.5, label=['Population histogram'], density=True,
             color="red")
    plt.show()

    wrapperC(population)


main()
