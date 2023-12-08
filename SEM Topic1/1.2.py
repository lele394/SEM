"""
q1:
confidence interval of 0.02, but conf interval is by convention 2*sigma, sigma the std-dev, so sigma = 0.01s

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

measures = 1000

def generate_data(mean, std_dev, num_values):
    # data = np.random.Generator.normal(mean, std_dev, num_values)
    data = norm.rvs(mean, std_dev, num_values)
    return data


pulls = generate_data(0, 0.01, measures)


# Create a histogram
hist, bins, __ =plt.hist(pulls, bins=30, alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Pulls')
plt.grid(True)

plt.show()


# Calculate the cumulative sum
cumulative_sum = [i/measures for i in np.cumsum(hist)]

# Create a plot for the cumulative sum
plt.figure()
plt.plot(bins[:-1], cumulative_sum, marker='o')
plt.xlabel('Value')
plt.ylabel('Cumulative Sum')
plt.title('Cumulative Sum of Histogram')

# get std-dev from the experimental pulls
std_dev = 0
for i in range(len(cumulative_sum)):
    if cumulative_sum[i]> 0.95:
        std_dev = bins[i]/2 #conf int = 2*sigma
        break

print(f'Std-dev for 1000 experimental pull is {std_dev}')

plt.show()




#question 3

print(" ===== Question 3 ======")

data = generate_data(0, 0.01, 100)
print(f'mean of the first 100 pull sequence : {sum(data)/len(data)}')
data = generate_data(0, 0.01, 100)
print(f'mean of the 2nd 100 pull sequence : {sum(data)/len(data)}')

# nope its not the same, but always close to 0


#question 4
print(" ===== Question 4 =====")
measures = 100
means = []
for means_to_do in range(1000):
    data = generate_data(0, 0.01, measures)
    means.append(sum(data)/len(data))


# Create a histogram
hist, bins, __ =plt.hist(means, bins=30, alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Means')
plt.grid(True)
plt.show()


cumulative_sum = [i/measures for i in np.cumsum(hist)]

# Create a plot for the cumulative sum
plt.figure()
plt.plot(bins[:-1], cumulative_sum, marker='o')
plt.xlabel('Value')
plt.ylabel('Cumulative Sum')
plt.title('Cumulative Sum of Histogram')
plt.show()

# get std-dev from the experimental pulls
std_dev = 0
for i in range(len(cumulative_sum)):
    if cumulative_sum[i]> 0.95:
        std_dev = bins[i]/2 #conf int = 2*sigma
        break

print(f'Std-dev of mean for 1000 sequence of 100 pull : {std_dev}')
"""

check chapter 2 for estimator of mean
use the sqrt formula, will find that the std-mean here is divided by around 10 compared to the previous one. 
because we do 1000 measures sqrt(1000/1) = 10


"""

print(f'Confidence interval is equal to std-dev*2 : {std_dev*2}')










