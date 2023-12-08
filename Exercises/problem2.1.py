import matplotlib.pyplot as plt
from random import random
import numpy as np

tries = 10000


def rand(proba):
    return random() < proba

Nall = [ 1, 4, 7, 10, 13, 16, 19]

pulls_master = [] # global pulls lists

# implement X
Xall = []
for N in Nall:
    X = [0 for i in range(N+1)]
    pulls = []

    for i in range(tries):
        p = []
        s = 0
        for j in range(N):
            if rand(0.5):
                s += 1
                p.append(0)
            else:
                p.append(1)
        X[s]+=1
        pulls.append(p)
    Xall.append(X)
    pulls_master.append(pulls)

    plt.plot([k for k in range(N+2)], np.array(X+[0]) * 1/tries)
plt.show()

def var(data):
    """var of a list"""
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    return variance



# b figure
variance = []
x_var = []
c = 0
for data in pulls_master:

    sub_sum = []
    for p in data:
        sub_sum.append(sum(p))

    variance.append(var(sub_sum))
    x_var.append(Nall[c])
    c += 1

#Nsigma²
plt.plot(  [0, 20], [0*0.25, 20*0.25 ]  )
# variance in dot
plt.plot(x_var, variance, marker="+", linestyle="")
plt.show()





#implement Z
for pulls in pulls_master:

    N = len(pulls[0])
    X = [0 for i in range(N+1)]
    Zns = [] #Zn for each pull serie
    print(N)

    foo = 0

    for pull in pulls:
        s = sum(pull)
        m = s/len(pull)
        Zn = (s-N*m) / np.sqrt(N*0.25)
        Zns.append(Zn)


    unique_values = [x for i, x in enumerate(Zns) if x not in Zns[:i]]

    print(unique_values)

    x_to_plot = []
    y_to_plot = []
    unique_values.sort()
    for i in unique_values:
        x_to_plot.append(Zns.count(i)/tries)
        y_to_plot.append(i)

    plt.plot(y_to_plot, x_to_plot)
plt.show()





















plt.show()
