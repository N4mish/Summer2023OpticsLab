import numpy as np

# constants
x_matrix = np.matrix([[0, 1],
                      [1, 0]])

y_matrix = np.matrix([[0, -1j],
                     [1j, 0]])

z_matrix = np.matrix([[1, 0],
                     [0, -1]])

# assumes eigenvalues are 1 and -1
def expect(zero, one):
    return (zero - one) / (zero + one)

def find_density_matrix(x_0, x_1, y_0, y_1, z_0, z_1):
    return (1/2) * ( np.identity(2)
                   + (expect(x_0, x_1) * x_matrix)
                   + (expect(y_0, y_1) * y_matrix)
                   + (expect(z_0, z_1) * z_matrix) )

x_0 = float(input("Input the count of 0 for X. "))
x_1 = float(input("Input the count of 1 for X. "))
y_0 = float(input("Input the count of 0 for Y. "))
y_1 = float(input("Input the count of 1 for Y. "))
z_0 = float(input("Input the count of 0 for Z. "))
z_1 = float(input("Input the count of 1 for Z. "))

res = find_density_matrix(x_0, x_1, y_0, y_1, z_0, z_1)
print(res)