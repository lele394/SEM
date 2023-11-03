from random import random
import matplotlib.pyplot as plt

def cont():
    input("press enter to continue")


# 1.1.2 Random number sequance generator
print("====== 1.1.2 For 1 sequence =====")

def random_pull(proba):
    return random() < proba


def random_sequence(n=1000):
    return [random_pull(0.5) for i in range(n)]


seq = random_sequence()

print(f'len {len(seq)}; mean {sum(seq)/len(seq)}')
print(f'number of YES : {sum(seq)}')

# cont()#break

number_of_seq = 500
x = [i for i in range(0,1000)]
y = [0 for i in range(0,1000)]
max, min = 0,1000

for i in range(number_of_seq):
    r = sum(random_sequence())
    y[r] += 1/number_of_seq
    if r > max: max = r
    if r < min: min = r

if True: #toggle
    plt.bar(x,y,  width=1, align='center')
    plt.xlim(min, max)
    plt.title("Distribution of YES for 500 sequenceS")
    plt.xlabel("Number of YES for a sequence of 1000 pulls")
    plt.ylabel("Amount of time it happend for 500 sequences")
    plt.show()


# cont()#break



# y.sort()
plt.xlim(min, max)
s_proba = []
c=0
for i in y:
    c+= i
    s_proba.append(c)




conf_interval = [0,0]
_s_pass = False
for i in range(len(s_proba)):
    if s_proba[i] > 0.05 and not _s_pass:
        print(f'cumulative sum pass 5% at {i}')
        _s_pass = True
        conf_interval[0] = i
        
    if s_proba[i] > 0.95:
        print(f'cumulative sum pass 95% at {i}')
        conf_interval[1] = i
        break

print(f'Confidence interval is between {conf_interval[0]/1000 * 100}% and {conf_interval[1]/1000 * 100}%. If probability is in this interval the sequence can be considered random.')

if True: # toggle
    plt.plot(x,s_proba)
    plt.xlabel("Number of YES for a sequence of 1000 pulls")
    plt.ylabel("Cumulative sum of probabilites")
    plt.title("Cumulative probabilities")
    plt.show()





#DO THE THEORY HERE







# redo everything for 4000 people poll

print(" ===== REDOES THE PREVIOUS TESTS BUT WITH POLLS OF 4000 PEOPLE =====")

number_of_seq = 500
x = [i for i in range(0,4000)]
y = [0 for i in range(0,4000)]
max, min = 0,4000

for i in range(number_of_seq):
    r = sum(random_sequence(4000))
    y[r] += 1/number_of_seq
    if r > max: max = r
    if r < min: min = r

if True: #toggle
    plt.bar(x,y,  width=1, align='center')
    plt.xlim(min, max)
    plt.title("Distribution of YES for 500 sequenceS")
    plt.xlabel("Number of YES for a sequence of 4000 pulls")
    plt.ylabel("Amount of time it happend for 500 sequences")
    plt.show()


# cont()#break



# y.sort()
plt.xlim(min, max)
s_proba = []
c=0
for i in y:
    c+= i
    s_proba.append(c)


conf_interval = [0,0]
_s_pass = False
for i in range(len(s_proba)):
    if s_proba[i] > 0.05 and not _s_pass:
        print(f'cumulative sum pass 5% at {i}')
        _s_pass = True
        conf_interval[0] = i
        
    if s_proba[i] > 0.95:
        print(f'cumulative sum pass 95% at {i}')
        conf_interval[1] = i
        break

print(f'Confidence interval is between {conf_interval[0]/4000 * 100}% and {conf_interval[1]/4000 * 100}%. If the probability is in this interval the sequence it can be considered random.')


if True: # toggle
    plt.plot(x,s_proba)
    plt.xlabel("Number of YES for a sequence of 4000 pulls")
    plt.ylabel("Cumulative sum of probabilites")
    plt.title("Cumulative probabilities")
    plt.show()


# poll have a +- 2% accurcay range when done on a sufficiently large group















