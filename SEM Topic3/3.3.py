import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

file_path = 'data.csv'  # Replace 'your_file.csv' with the path to your CSV file

# Initialize an empty list to hold the data
matrix = []
# Open the CSV file and read its contents
with open(file_path, 'r') as file:

    data = file.read()
    l = data.split("\n")
    l.pop(0)
    for line in l:
        matrix.append([int(i) for i in line.split(";")[2:-1]])



#helper function
def printm(matrix):
    print(f'{len(matrix)}x{len(matrix[0])}')
    for i in matrix:
        print(i)




def showm(matrix_data):
    # Display the matrix using matshow
    plt.matshow(matrix_data, cmap='viridis')  # 'viridis' is a colormap, you can choose others
    plt.colorbar()  # Display a color bar showing the scale
    plt.title('Matrix Visualization')  # Title for the plot
    plt.show()










M = np.array(matrix)

M_bar = np.tile(np.mean(M, axis=0), (19,1))

Mc = M - M_bar

C = np.cov(M, rowvar=False)

# eigenvlaues, eigenvectors
Dl, V = linalg.eigh(C)

D = np.zeros([len(Dl),len(Dl)])
for i in range(len(Dl)):
    for j in range(len(Dl)):
        if i ==j:
            D[i,j] = Dl[i]

R = np.corrcoef(M, rowvar=False)

Y = np.matmul(Mc, V)

Z = Y[:, -3:]
psi = np.transpose(V)[-3:, :]
# isolates the 3 most prominent values



print(f'Y   {len(Y)}x{len(Y[0])}')
print(f'Z   {len(Z)}x{len(Z[0])}')
print(f'psi {len(psi)}x{len(psi[0])}')
print(f'm_bar {len(M_bar)}x{len(M_bar[0])}')







#  Question 1
sub = np.matmul(Z, psi) 
print(f'sub {len(sub)}x{len(sub[0])}')

truncated_matrix =  M_bar + sub

print(f'M_trunc {len(truncated_matrix)}x{len(truncated_matrix[0])}')

"""
#  Compare those 2 here
plt.matshow(truncated_matrix, cmap='viridis', label="truncated")
plt.matshow(M, cmap='viridis', label="original")
# plt.matshow(Mc, cmap='viridis', label="Mc")
plt.show()
"""

# showm(Y)





#  Question 2
loss_factor = sum(Dl[:7])/sum(Dl)
print(f'Loss factor is of about {loss_factor}')





#3D plot of R

#3D plot
import matplotlib.pyplot as plt
import numpy as np

columns = ["1500 m", "100 m", "400 m", "110 m hurdles", "Long jump", "Shot put", "High jump", "Discus throw", "Pole vault", "Javelin throw"]
x=np.array([i for i in range(len(R))])
y=np.array([j for j in range(len(R[0]))])
z=[]
x, y = np.meshgrid(x, y)

for i in range(len(R)):
    sub = []
    for j in range(len(R[0])):
        sub.append(R[i][j])
    z.append(sub)
z = np.array(z)

#viridis 3D matrix
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', linewidth=0, antialiased=False)
# ax.set_zlim(0, 1.01)
plt.xticks(range(len(columns)), columns, rotation = 0)
plt.yticks(range(len(columns)), columns, rotation = 0)
plt.show()

#2D grayscale matrix
plt.matshow(R, cmap='gist_gray')  # 'viridis' is a colormap, you can choose others
plt.colorbar()  # Display a color bar showing the scale
plt.title('Correlation matrix')  # Title for the plot
plt.xticks(range(len(columns)), columns, rotation = 90)
plt.yticks(range(len(columns)), columns, rotation = 0)
plt.show()




#question 4
sub = V.T[7:10, :]
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
for i in range(len(columns)):
    x = sub[0, i]
    y = sub[1, i]
    z = sub[2, i]
    ax.plot([0, x], [0, y], [0, z], label=columns[i])

plt.legend()
plt.show()



#question 5
#pareil que question 4

#question 6
print("question 5")
lines = np.array(["Warner","Mayer","Moloney","Scantling","Lepage","Ziemek","Victor","Shkurenyov","Urena","Bastien","Erm","Wiesiolek","Zhuk","Kazmirek","Uibo","Helcelet","Sykora","Dos Santos","Roe"])

sub = Y[:, 7:10]
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
for i in range(len(lines)):
    x = sub[i, 0]
    y = sub[i, 1]
    z = sub[i, 2]
    ax.plot([0, x], [0, y], [0, z], label=lines[i])

plt.legend()
plt.show()
