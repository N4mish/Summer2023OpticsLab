#make a best fit plot of a cos squared function A*cos^2(x+B)+C
#with a given set of data points

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
from scipy.optimize import curve_fit

#data points
x = []
y = []
z = []

xdata = np.array([])
ydata = np.array([52, 650, 21, 181, 219, 720, 425, 585])

# convert to radians

def deg2rad(deg):
    return deg*np.pi/180

col1 = 'HWP 1 Angle'
col2 = 'HWP 2 Angle'
col3 = 'Detector 4'
col4 = 'Detector 3'

xmap = {}
zmap = {}

# reading csv file
with open('Data\June 23\HWP_Combined.csv', newline='') as csvfile: # this is a Windows path. If using UNIX based systems change accordingly
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row[col1] != '' and row[col2] != '' and row[col3] != '' and row[col4] != ''): # avoids blank lines
            x.append(float(row['Polarizer Angle']))
            y.append(float(row['HWP Angle']))
            z.append(float(row['Power']))
            if (not (float(row['HWP Angle'])) in xmap):
                xmap[float(row['HWP Angle'])] = []
            xmap[float(row['HWP Angle'])].append(float(row['Polarizer Angle']))
            if (not (float(row['HWP Angle'])) in zmap):
                zmap[float(row['HWP Angle'])] = []
            zmap[float(row['HWP Angle'])].append(float(row['Power']))

# numpy-ify the x and y data
xdata = np.array(x)
ydata = np.array(y)
zdata = np.array(z)


#function to fit
def cos2(x, A, B, C):
    return A*np.cos(x+B)**2 + C

def cos3D(data, A, B, C):
    x = deg2rad(data[0])
    y = deg2rad(data[1])
    return A*np.cos(2*y - x + B)**2 + C

# #fit the data
popt, pcov = curve_fit(cos3D, [x, y], z)


#plot the data and the fit
fig = plt.figure(1)

ax = fig.add_subplot(projection='3d')

# small dictionary to map HWP angles to colors
colors = {}
colors[0] = 'red'
colors[22.5] = 'orange'
colors[45] = 'yellow'
colors[67.5] = 'green'
colors[90] = 'blue'
colors[112.5] = 'purple'


# scatterplotting the points
for key in xmap:
    ax.scatter(xmap[key], key, zmap[key], color=colors[key])

ax.set_xlabel('Polarizer Angle (degrees)')
ax.set_ylabel('HWP Angle (degrees)')
ax.set_zlabel('Power (microwatts)')


# create surface function model
# setup data points for calculating surface model
model_x_data = np.linspace(min(xdata), max(xdata), 30)
model_y_data = np.linspace(min(ydata), max(ydata), 30)
# create coordinate arrays for vectorized evaluations
X, Y = np.meshgrid(model_x_data, model_y_data)
# calculate Z coordinate array
Z = cos3D(np.array([X, Y]), *popt)

ax.plot_surface(X, Y, Z, alpha=0.5)

print(f"A = {popt[0]}, B = {popt[1]}, C = {popt[2]}")

plt.show() 