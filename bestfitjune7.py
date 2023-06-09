#make a best fit plot of a cos squared function A*cos^2(x+B)+C
#with a given set of data points

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

#data points
x = []
y = []

# convert to radians

def deg2rad(deg):
    return deg*np.pi/180

# reading csv file
with open('Data\Jun7PolariationFit.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row['Angle'] != '' and row['Power'] != ''):
            x.append(deg2rad(float(row['Angle'])))
            y.append(float(row['Power']))
        #x.append(float(row['Angle']))
        #y.append(float(row['Power']))

# numpy-ify the x and y data
xdata = np.array(x)
ydata = np.array(y)

#function to fit
def cos2(x, A, B, C):
    return A*np.cos(x+B)**2 + C

#fit the data
popt, pcov = curve_fit(cos2, xdata, ydata)

#plot the data and the fit
plt.figure(1)
plt.plot(xdata, ydata, 'o', label='Power Transmitted')
plt.legend()

#output the fit parameters
print(f"Power Transmitted: A = {popt[0]}, B = {popt[1]}, C = {popt[2]}")
#plot the data with the equation of the fit
plt.figure(2)
plt.plot(xdata, ydata, 'o', label='Power Transmitted')
#plot the equation of the fit over a range of x values
plt.plot(np.linspace(0, 6, 100), cos2(np.linspace(0, 6, 100), *popt), label='Transmitted fit', color = 'orange', alpha = 0.5)

plt.legend()
plt.show()