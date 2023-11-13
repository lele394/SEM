import numpy as np
import matplotlib.pyplot as plt

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
Dl, V = np.linalg.eigh(C)

D = np.zeros([len(Dl),len(Dl)])
for i in range(len(Dl)):
    for j in range(len(Dl)):
        if i ==j:
            D[i,j] = Dl[i]






R = np.corrcoef(M)

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


#  Compare those 2 here
plt.matshow(truncated_matrix, cmap='viridis', label="M_trunc")
plt.matshow(M, cmap='viridis', label="M")
# plt.matshow(Mc, cmap='viridis', label="Mc")
plt.show()


# showm(Y)





#  Question 2
loss_factor = sum(Dl[:3])/sum(Dl)
print(f'Loss factor is of about {loss_factor}')




