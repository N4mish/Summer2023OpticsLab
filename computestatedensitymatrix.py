import numpy as np
from statetomography import fidelity, state_tomo

def deg2rad(deg):
    return deg*np.pi/180


def hwp(theta):
    theta = deg2rad(theta)
    return np.matrix([[np.cos(2 * theta),     np.sin(2 * theta)], 
                     [np.sin(2 * theta),     -1*np.cos(2 * theta)]])


def qwp(theta):
    theta = deg2rad(theta)
    return np.matrix([[(np.cos(theta) ** 2) + (1j * np.sin(theta) ** 2),    (1 - 1j) * np.sin(theta) * np.cos(theta)],
                     [(1 - 1j) * np.sin(theta) * np.cos(theta),         np.sin(theta) ** 2 + 1j * np.cos(theta) ** 2]])


if (__name__ == "__main__"):
    hwpangle = float(input("Please input the HWP angle. "))
    qwpangle = float(input("Please input the QWP angle. "))

    statevec = np.matmul(qwp(qwpangle), np.matmul(hwp(hwpangle), np.matrix([[1], [0]])))

    print(f"statevector:\n{statevec}")

    ideal = np.matmul(statevec, statevec.getH())

    print(f"density matrix:\n{np.matmul(statevec, statevec.getH())}")

    experimental = state_tomo()

    print(f"experimental:\n{experimental}")

    print(f"fidelity: {fidelity(experimental, ideal)}")
