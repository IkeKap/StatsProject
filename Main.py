# Credits for some snippets of code to https://github.com/dandrewmyers/numerical/blob/master/mc_pi.py

import matplotlib.pyplot as plt
import numpy as np
import math as m
import xlsxwriter as xlsx
import time as time # to show time to calculate

# input total number of random points
total_random_points = int(input("\nNumber of random points for Monte Carlo estimate of Pi?\n>"))

# start time of calculation
start_time = time.time()

# name for new workbook. Convention will be (Trial length)Pi(Trial Number)
name = str(total_random_points) + 'Pi1'
# setting up an Excel workbook for the project
workbook = xlsx.Workbook(name)
worksheet = workbook.add_worksheet()

# number of random points inside unit cicrle and total random points
inside_circle = 0

# create empty x and y arrays for eventual scatter plot of generated random points
x_plot_array = np.empty(shape=(1,total_random_points))
y_plot_array = np.empty(shape=(1,total_random_points))

# create specific X and Y arrays for color rules
x_inside_plot_array = np.empty(shape=(1,total_random_points))
x_outside_plot_array = np.empty(shape=(1,total_random_points))

y_inside_plot_array = np.empty(shape=(1,total_random_points))
y_outside_plot_array = np.empty(shape=(1,total_random_points))

# generate random points and count points inside unit circle
# top right quadrant of unit cicrle only
for i in range(0, total_random_points):
    # generate random x, y in range [0, 1]
    x = np.random.rand()
    x_plot_array = np.append(x_plot_array, [x])
    y = np.random.rand()
    y_plot_array = np.append(y_plot_array, [y])
    # calc x^2 and y^2 values
    x_squared = x**2
    y_squared = y**2
    # count if inside unit circle, top right quadrant only
    if np.sqrt(x_squared + y_squared) < 1.0:
        inside_circle += 1
        x_inside_plot_array = np.append(x_inside_plot_array,[x])
        y_inside_plot_array =np.append(y_inside_plot_array,[y])
    else:
        x_outside_plot_array= np.append(x_outside_plot_array,[x])
        y_outside_plot_array = np.append(y_outside_plot_array, [y])
    # calc approximate pi value
    pi_approx = inside_circle / (i+1) * 4

# final numeric output for pi estimate. Outputted to terminal window. 
print ("\n--------------")
print (f"\nApproximate value for pi: {pi_approx}")
print (f"Difference to exact value of pi: {pi_approx-np.pi}")
print (f"Percent Error: (approx-exact)/exact*100: {(pi_approx-np.pi)/np.pi*100}%")
print (f"Execution Time: {time.time() - start_time} seconds\n")

# plot output of random points and circle. 
inside_circle_plot = plt.scatter(x_inside_plot_array,y_inside_plot_array, color='blue', s=.1)
outside_circle_plot = plt.scatter(x_outside_plot_array,y_outside_plot_array, color='red', s=.1)
circle_plot = plt.Circle( ( 0, 0 ), 1, color='black', linewidth=2, fill=False)

ax = plt.gca()
ax.cla()

ax.add_artist(inside_circle_plot)
ax.add_artist(outside_circle_plot)
ax.add_artist(circle_plot)

plt.show()