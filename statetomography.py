import numpy as np
import scipy.linalg as sp
# constants
x_matrix = np.matrix([[0, 1],
                      [1, 0]])

y_matrix = np.matrix([[0, -1j],
                     [1j, 0]])

z_matrix = np.matrix([[1, 0],
                     [0, -1]])

'''
assumes eigenvalues are 1 and -1
'''
def expect(zero, one):
    return (zero - one) / (zero + one)

'''
returns a density matrix of the state.
assumes that the 
'''
def state_tomo():
    x_0 = float(input("Input the count of 0 for X. "))
    x_1 = float(input("Input the count of 1 for X. "))
    y_0 = float(input("Input the count of 0 for Y. "))
    y_1 = float(input("Input the count of 1 for Y. "))
    z_0 = float(input("Input the count of 0 for Z. "))
    z_1 = float(input("Input the count of 1 for Z. "))
    return (1/2) * ( np.identity(2)
                   + (expect(x_0, x_1) * x_matrix)
                   + (expect(y_0, y_1) * y_matrix)
                   + (expect(z_0, z_1) * z_matrix) )

'''
given two density matrices, computes fidelity. 
'''
def fidelity(rho, sigma):
    return np.real(np.trace(sp.sqrtm(np.matmul(sp.sqrtm(sigma), np.matmul(rho, sp.sqrtm(sigma)))))) ** 2


if __name__ == "__main__":
    denMat1 = state_tomo()

    response = input("Type Y if you would like to enter information for a second matrix.").lower()

    if (response == 'y'):
        denMat2 = state_tomo()

        print(f"matrix 1: \n{denMat1}\n matrix 2: \n{denMat2}")

        response = input("Type Y if you would like to measure fidelity.").lower()
        if (response == 'y'):
            print(f"fidelity: {np.real(fidelity(denMat1, denMat2))}")

    else:
        print(f"matrix: \n{denMat1}")






