from computestatedensitymatrix import hwp, qwp, deg2rad
import numpy as np

mat = np.matrix([[1],
                 [0]])

mat = np.matmul(qwp(45), np.matmul(hwp(0), mat))

print(mat)
