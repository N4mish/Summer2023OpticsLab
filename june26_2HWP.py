#make a best fit plot of a cos squared function A*cos^2(x+B)+C
#with a given set of data points

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
from scipy.optimize import curve_fit

# functions to fit
def func1(data, A, B, C):
    x = deg2rad(data[0])
    y = deg2rad(data[1])
    return A*np.cos(2*(x - y) + B) ** 2 + C

def func2(data, A, B, C, D):
    x, y = deg2rad(data[0]), deg2rad(data[1])
    return (1/4)*A*(2 + np.cos(4*x + B) + np.cos(4*x - 4*y + D)) + C

check = input("What data would you like to see? Type HWP or QWP.").lower().strip()

if check == 'hwp':
    f = 'Data\June 23\HWP_Combined.csv'
    func = func1
else:
    f = 'Data\June 26\QWP_Combined.csv'
    func = func2



#data points
x = []
y = []
z1 = []
z2 = []

xdata = np.array([])
ydata = np.array([52, 650, 21, 181, 219, 720, 425, 585])

# convert to radians

def deg2rad(deg):
    return deg*np.pi/180

col1 = 'HWP 1 Angle'
col2 = 'HWP 2 Angle'
col3 = 'Detector 4'
col4 = 'Detector 3'

# maps the X to certain values
y_map = {}
z1_map = {}
z2_map = {}

def addToMap(map, key, val):
    if key not in map:
        map[key] = []
    map[key].append(val)
    
# reading csv file
with open(f, newline='') as csvfile: # this is a Windows path. If using UNIX based systems change accordingly
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row[col1] != '' and row[col2] != '' and row[col3] != '' and row[col4] != ''): # avoids blank lines
            x.append(float(row[col1]))
            y.append(float(row[col2]))
            z1.append(float(row[col3]))
            z2.append(float(row[col4]))
            addToMap(y_map, float(row[col1]), float(row[col2]))
            addToMap(z1_map, float(row[col1]), float(row[col3]))
            addToMap(z2_map, float(row[col1]), float(row[col4]))

# numpy-ify the data
xdata = np.array(x)
ydata = np.array(y)
z1data = np.array(z1) # Horizontal
z2data = np.array(z2) # Vertical

# #fit the data
popt, pcov = curve_fit(func, [x, y], z1)
popt2, pcov2 = curve_fit(func, [x, y], z2)


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

for key in y_map:
    ax.scatter(key, y_map[key], z1_map[key], color=colors[key])

ax.set_xlabel('HWP 1 Angle (degrees)')
ax.set_ylabel('HWP 2 Angle (degrees)')
ax.set_zlabel('Counts')


# create surface function model
# setup data points for calculating surface model
model_x_data = np.linspace(min(xdata), max(xdata), 30)
model_y_data = np.linspace(min(ydata), max(ydata), 30)
# create coordinate arrays for vectorized evaluations
X, Y = np.meshgrid(model_x_data, model_y_data)
# calculate Z coordinate array
Z = func(np.array([X, Y]), *popt)

ax.plot_surface(X, Y, Z, alpha=0.5)

print(f"A = {popt[0]}, B = {popt[1]}, C = {popt[2]}")

plt.show() 