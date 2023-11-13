# 2.1.1 background

import statistics
from scipy.optimize import curve_fit
from scipy.stats import norm, chi2
from matplotlib import pyplot as plt
import numpy as np



# question 1
# defining lists
T = [ 1.925 + 0.05*i for i in range(13)]
N = [19, 19, 39, 48, 87, 94, 104, 92, 57, 44, 28, 26, 13]

data = []
for i in range(len(N)):
    for j in range(N[i]):
        data.append(T[i])

# meanT = sum(T)/len(T)
# meanN = sum(N)/len(N)
mean_data = sum(data)/len(data)
# print(f'mean of T ={meanT}')
# print(f'mean of T ={meanN}')
print(f'mean of T ={mean_data}')
# stdevT = statistics.stdev(T)
# stdevN = statistics.stdev(N)
stdev_data = statistics.stdev(data)
# print(f'stdev of T ={stdevT}')
# print(f'stdev of T ={stdevN}')
print(f'stdev of T ={stdev_data}')





# create N_sum
N_sum = np.cumsum(N)
# normal law
pdf = norm.pdf(T, loc=mean_data, scale=stdev_data)
cdf = norm.cdf(T, loc=mean_data, scale=stdev_data)

n_pdf = pdf/max(pdf)*max(N)

# question 2
if False: #toggle

    # histogram
    fig, axes = plt.subplots(1,2)
    axes[0].bar(T,N, width=0.05, align='center', label="data")
    axes[0].set_title("Number of light per flight-time")
    axes[0].set_xlabel("Flight time")
    axes[0].set_ylabel("Number of flights")


    # cumulative distribution
    axes[1].plot(T,N_sum, label='data') # just a curve
    # axes[1].bar(T,N_sum, width=0.05, align='center', label="data") # histogram-style
    axes[1].set_title("Cumulative number of flight per flight-time")
    axes[1].set_xlabel("Flight time")
    axes[1].set_ylabel("Total number of flights")


    # comparison to normal law
    #plot that on the corresponding graphs
    axes[0].bar(T, n_pdf, width=0.05, align='center', label="normal law", alpha=0.6)
    axes[1].plot(T, cdf*max(N_sum), label="normal law")
    # axes[1].bar(T, cdf, width=0.05, align='center', label="normal law")




    plt.tight_layout()
    axes[1].legend()

    plt.show()



# question 3
D = np.sum(([(a - b)**2/b for a, b in zip(N, n_pdf)]))
print("D^2:", D)



# question 4
dof = 12 # degrees of freedom
p_value = 1-chi2.cdf(D, dof)

print("P-Value:", p_value)

if p_value<0.05: # 0.05 is the condition for the 95% interval, if under that, we can reject the hypothesis
    print("p value is under 0.05, we can reject the hypothesis that it is a gaussian.")
else:
    print("p value is above 0.05, we can't reject the hypothesis that it is a gaussian.")





# 2.2 here and not in another 

#question 1
def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))



initial_guess = [max(n_pdf), mean_data, stdev_data]
params, covariance = curve_fit(gaussian, T, N, p0=initial_guess)
A, mu, sigma = params

# for graphing
nbpts = 300
a = 1.8
b = 2.6
x = [a + i * (b - a) / (nbpts - 1) for i in range(nbpts)]

formatted_string = f'Fitted curve parameters are :\n A = {A:.3f}\n mu = {mu:.3f}\n sigma = {sigma:.3f}'
print(formatted_string)

if True: # toggle
    plt.plot(T, N, label="given data", linestyle="", marker="x")
    plt.plot(x, [gaussian(i, initial_guess[0], initial_guess[1], initial_guess[2]) for i in x], label="initial gaussian")
    plt.plot(x, [gaussian(i, A, mu, sigma) for i in x], label="fitted curve")
    plt.text(1.8, 85, formatted_string, fontsize=9, color='black')
    plt.legend()
    plt.show()



# question 2
# we use the convariance outputted in the previous question
print(f'Covariance matrix of the fit \n{covariance}')
# Get the standard errors (uncertainties) for A, mu, and sigma
std_err_A, std_err_mu, std_err_sigma = np.sqrt(np.diag(covariance))
print(f'Uncertainties :\n U_A : {2*std_err_A}\n U_mu : {2*std_err_mu}\n U_sigma : {2*std_err_sigma}')
















#