import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = [] # col 1 data
y = [] # col 2 data
z = [] # col 3 data

# the following make scattering the data a little nicer.
ymap = {} # col 2 mapped with x as key
zmap = {} # col 3 mapped with x as key

file = 'Data\June 16\photoncounts.csv'

def deg2rad(deg):
    return deg*np.pi/180


col1 = 'HWP Angle'
col2 = 'Horizontal'
col3 = 'Vertical'

# reading csv file
with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row[col1] != '' and row[col2] != '' and row[col3] != ''):
            x.append((float(row[col1])))
            y.append((float(row[col2])))
            z.append(float(row[col3]))
            if (not (float(row[col1])) in ymap):
                ymap[float(row[col1])] = []
            ymap[float(row[col1])].append((float(row[col2])))
            if not float(row[col1]) in zmap:
                zmap[float(row[col1])] = []
            zmap[float(row[col1])].append((float(row[col3])))

# numpy-ify the data
xdata = np.array(x)
ydata = np.array(y)
zdata = np.array(z)

fig = plt.figure(1)
ax = fig.add_subplot()

# function to fit to
def sin(x, A, B, C):
    x = deg2rad(x)
    return A*np.sin(2*x + B) ** 2 + C
# scatterplotting the points
ax.scatter(xdata, ydata, label = 'Horizontal', color = 'red')

ax.scatter(xdata, zdata, label = 'Vertical', color = 'blue')

# curve fitting
horiz_popt, horiz_pcov = curve_fit(sin, x, y)
vert_popt, vert_pcov = curve_fit(sin, x, z)

print(sin(0, *horiz_popt))

ax.set_xlabel('HWP Angle')
ax.set_ylabel('Counts')

plt.plot(np.linspace(0, 180, 360), sin(np.linspace(0, 180, 360), *horiz_popt), label='Horizontal fit', color = 'red', alpha = 0.5)
plt.plot(np.linspace(0, 180, 360), sin(np.linspace(0, 180, 360), *vert_popt), label='Vertical fit', color = 'blue', alpha = 0.5)

print(f"Horizontal: A = {horiz_popt[0]}, B = {horiz_popt[1]}, C = {horiz_popt[2]}")
print(f"Vertical: A = {vert_popt[0]}, B = {vert_popt[1]}, C = {vert_popt[2]}")

plt.legend()
plt.show()