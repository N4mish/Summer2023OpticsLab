#make a best fit plot of a cos squared function A*cos^2(x+B)+C
#with a given set of data points

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#data points
xdata = np.array([0, 4.18879, 2.635447, 0.261799, 5.393067, 1.466077, 3.804818])
ydata = np.array([148, 320, 85, 215, 109, 270, 300])

#order the data points based on y value
ydata = ydata[np.argsort(xdata)]
xdata = np.sort(xdata)


#function to fit
def cos2(x, A, B, C):
    return A*np.cos(x+B)**2 + C

#fit the data
popt, pcov = curve_fit(cos2, xdata, ydata)

#plot the data and the fit
plt.plot(xdata, ydata, 'o', label='data')
plt.legend()
plt.show()

#output the fit parameters
print(f"A = {popt[0]}, B = {popt[1]}, C = {popt[2]}")
#plot the data with the equation of the fit
plt.plot(xdata, ydata, 'o', label='data')
#plot the equation of the fit over a range of x values
plt.plot(np.linspace(0, 6, 100), cos2(np.linspace(0, 6, 100), *popt), label='fit')
plt.legend()
plt.show()


