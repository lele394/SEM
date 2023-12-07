
from numpy.random import normal
from matplotlib import pyplot as plt

def Xbar(x):
    return sum(x)/len(x)

def Sn2(x):
    s = 0
    Xb = Xbar(x)
    for xi in x:
        s += (xi-Xb)**2
    return s/len(x)


def Sn_12(x):
    s = 0
    Xb = Xbar(x)
    for xi in x:
        s += (xi-Xb)**2
    return s/(len(x)-1)


pulls = 10
tests = 100

mean = 0
stdev = 0.5

sn2_results = []
sn_12_results = []


for test in range(tests):

    serie = normal(mean, stdev, pulls)

    sn2_results.append(Sn2(serie))
    sn_12_results.append(Sn_12(serie))


plt.plot([i for i in range(tests)], sn2_results, label="Sn2")
plt.plot([i for i in range(tests)], sn_12_results, label="Sn_12")
plt.legend()
plt.show()

"""
Test with different number of pulls. The smaller the amount, the 
bigger the gap. This is due to the mathematical impact of n-1 in the formula

"""