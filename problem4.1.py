import scipy.stats as stats
import matplotlib.pyplot as plt




print("\n\n\n QUESTION 1 & 2 \n\n\n")


n = 20 #puls
p = 0.5 # probability

l = [] # container list
for i in range(n+1): # loop til 20
    proba = stats.binom.pmf(i, n, p)
    l.append([i, proba]) # appends the i and the proba

print("number of head  | probability") # print the table
for i in l:
    print(f'\t{i[0]}\t| {round(i[1], 8)}')

# plt.plot([i[0] for i in l],[i[1] for i in l])
# plt.show()




# q2 
s = 0
for i in l:
    if not(i[0]> 8 and i[0]<12): # sums all except 9, 10 ,11
        # print(i)
        s+= i[1]

print(f'\n\nsum of all probabilities except 9, 10 and 11 : {s}')








# q5

print("\n\n\n QUESTION 5 \n\n\n")

n = 4865+5135
p = 0.5

l = []
for i in range(n+1):
    proba = stats.binom.pmf(i, n, p)
    l.append([i, proba])

# print("number of head  | probability")
# for i in l:
#     print(f'\t{i[0]}\t| {round(i[1], 8)}')

# plt.plot([i[0] for i in l],[i[1] for i in l])
# plt.show()





s = 0
for i in l:
    if not(i[0]> 4865 and i[0]<5135):
        # print(i)
        s+= i[1]

print(f'\n\nsum of all probabilities except 9, 10 and 11 : {s}')