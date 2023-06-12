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

xmap = {}
zmap = {}
# convert to radians

def deg2rad(deg):
    return deg*np.pi/180

col1 = 'HWP Angle'
col2 = 'QWP Angle'
col3 = 'Horizontal Power'

# reading csv file
with open('Data\June12\P-HWP-QWP - Sheet1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    xmap[1234] = []
    zmap[1234] = []
    for row in reader:
        if (row[col1] != '' and row[col2] != '' and row[col3] != ''):
            x.append(deg2rad(float(row[col1])))
            y.append(deg2rad(float(row[col2])))
            y2.append(float(row[col3]))
            if (not (float(row[col1])) in xmap):
                xmap[float(row[col1])] = []
            xmap[float(row[col1])].append((float(row[col2])))
            if not float(row[col1]) in zmap:
                zmap[float(row[col1])] = []
            zmap[float(row[col1])].append((float(row[col3])))
            if (row["Horizontal Power 785"] != ''):
                xmap[1234].append(float(row[col2]))
                zmap[1234].append(float(row["Horizontal Power 785"]))


# numpy-ify the x and y data
xdata = np.array(x)
ydata = np.array(y)
y2data = np.array(y2)

#function to fit
def HWPQWPPower(data, A, B, C, D):
    phi = data[0]
    theta = data[1]
    return A*np.cos(phi + D)**2*np.cos(theta + B)**4 + A*np.cos(phi + D)**2*np.sin(theta + B)**4 + C

#fit the data
popt, pcov = curve_fit(HWPQWPPower, ydata, y2data)

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
colors[135] = 'black'
colors[157.5] = 'cyan'
colors[180] = 'magenta'

# scatterplotting the points
for key in xmap:
    if key != 1234:
        ax.scatter(xmap[key], key, zmap[key], color=colors[key])

ax.set_xlabel('HWP Angle')
ax.set_ylabel('QWP Angle')
ax.set_zlabel('Power (microwatts)')


# create surface function model
# setup data points for calculating surface model
model_x_data = np.linspace(min(xdata), max(xdata), 30)
model_y_data = np.linspace(min(ydata), max(ydata), 30)
# create coordinate arrays for vectorized evaluations
X, Y = np.meshgrid(model_x_data, model_y_data)
# calculate Z coordinate array
Z = HWPQWPPower(np.array([X, Y]), *popt)

# ax.plot_surface(X, Y, Z, alpha=0.5)

print(f"A = {popt[0]}, B = {popt[1]}, C = {popt[2]}")


plt.figure(2)
plt.plot(xmap[1234], zmap[1234], 'o', label='785nm')
plt.plot(xmap[0], zmap[0], 'o', label="400nm")
plt.legend()

plt.show() 
