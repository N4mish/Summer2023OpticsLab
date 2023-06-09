#make a best fit plot of a cos squared function A*cos^2(x+B)+C
#with a given set of data points

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

#data points
x = []
y = []
y2 = []
# convert to radians

def deg2rad(deg):
    return deg*np.pi/180

# reading csv file
with open('Data\June9\Polarizer HWP PBS.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row['HWP Angle'] != '' and row['Power Transmitted'] != '' and row['Power Reflected'] != ''):
            x.append(deg2rad(float(row['HWP Angle'])))
            print(f"rad: {deg2rad(float(row['HWP Angle']))} --- deg: {float(row['HWP Angle'])}")
            y.append(float(row['Power Transmitted']))
            y2.append(float(row['Power Reflected']))
        #x.append(float(row['Angle']))
        #y.append(float(row['Power']))

# numpy-ify the x and y data
xdata = np.array(x)
ydata = np.array(y)
y2data = np.array(y2)

#function to fit
def cos2(x, A, B, C):
    return A*np.cos(2*x+B)**2 + C

#fit the data
popt, pcov = curve_fit(cos2, xdata, ydata)

popt2, pcov2 = curve_fit(cos2, xdata, y2data)
#plot the data and the fit
plt.figure(1)
plt.plot(xdata, ydata, 'o', label='Power Transmitted', color='red')
plt.plot(xdata, y2data, 'o', label='Power Reflected', color='blue')
plt.legend()

#output the fit parameters
print(f"Power Transmitted: A = {popt[0]}, B = {popt[1]}, C = {popt[2]}")
print(f"Power Reflected: A = {popt2[0]}, B = {popt2[1]}, C = {popt2[2]}")
#plot the data with the equation of the fit
plt.figure(2)
plt.plot(xdata, ydata, 'o', label='Power Transmitted', color='red')
plt.plot(xdata, y2data, 'o', label='Power Reflected', color='blue')
#plot the equation of the fit over a range of x values
plt.plot(np.linspace(0, 3.3, 100), cos2(np.linspace(0, 3.3, 100), *popt), label='Transmitted fit', color = 'orange', alpha = 0.5)
plt.plot(np.linspace(0, 3.3, 100), cos2(np.linspace(0, 3.3, 100), *popt2), label='Reflected fit', color = 'purple', alpha = 0.5)

plt.legend()
plt.show()