import numpy as np
from scipy.linalg import sqrtm
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

def state_tomo(x_0, x_1, y_0, y_1, z_0, z_1):
    return (1/2) * ( np.identity(2)
                   + (expect(x_0, x_1) * x_matrix)
                   + (expect(y_0, y_1) * y_matrix)
                   + (expect(z_0, z_1) * z_matrix) )

def fidelity(rho, sigma):
    return np.trace(sqrtm(np.matmul(sqrtm(sigma), np.matmul(rho, sqrtm(sigma)))))

x_0 = float(input("Input the count of 0 for X. "))
x_1 = float(input("Input the count of 1 for X. "))
y_0 = float(input("Input the count of 0 for Y. "))
y_1 = float(input("Input the count of 1 for Y. "))
z_0 = float(input("Input the count of 0 for Z. "))
z_1 = float(input("Input the count of 1 for Z. "))

denMat1 = state_tomo(x_0, x_1, y_0, y_1, z_0, z_1)


response = input("Type Y if you would like to enter information for a second matrix.").lower()

if (response == 'y'):
    x_01 = float(input("Input the count of 0 for X. "))
    x_11 = float(input("Input the count of 1 for X. "))
    y_01 = float(input("Input the count of 0 for Y. "))
    y_11 = float(input("Input the count of 1 for Y. "))
    z_01 = float(input("Input the count of 0 for Z. "))
    z_11 = float(input("Input the count of 1 for Z. "))

    denMat2 = state_tomo(x_01, x_11, y_01, y_11, z_01, z_11)

    print(f"matrix 1: \n{denMat1}\n matrix 2: \n{denMat2}")

    response = input("Type Y if you would like to measure fidelity.").lower()
    if (response == 'y'):
        print(f"fidelity: {np.real(fidelity(denMat1, denMat2))}")

else:
    print(f"matrix: \n{denMat1}")






