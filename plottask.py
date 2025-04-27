'''Write a program called plottask.py that displays:

a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.
Some marks will be given for making the plot look nice (legend etc).

Please put a copy of the image of the plot (.png file) into the repository'''

import matplotlib.pyplot as plt
import numpy as np

# generate random data points with mean of 5, standard deviation of 2, and 1000 data points.
# followed structure here: https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html 
data = np.random.normal(loc=5, scale=2, size = 1000)

# instructions say plot range of 0 to 10 but didnt say number of entries.
# Used linspace because it returns evenly spaced numbers.
# https://numpy.org/doc/2.1/reference/generated/numpy.linspace.html

x = np.linspace(0,10)

# h is x**3. x is set above so h is based on x. h(x)=x3 means take each value of x and cube it, giving the corresponding value of h. I've seen Ian do this in principles of DA so that's my understanding of it.
h = x**3

# create the figure and axes. copied this from my principles of DA notes where i put a few hists on one plot for my tasks.
fig, ax1 = plt.subplots()

# all basic plot code adapted from: https://matplotlib.org/stable/tutorials/pyplot.html 
# this has info on plotting two things "overlayed" which i adapted for a hist instead of two lines:
# https://stackoverflow.com/questions/43179027/multiple-plots-in-same-figure-with-one-axis-via-python-matplotlib

#plot a histogram. i want the edges to have black outline, add generic label for now.
ax1.hist(data, edgecolor = "black", label="Normal Distribution")
ax1.set_xlabel("values") # dont have meaningful label
ax1.set_ylabel("Frequency", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# twinx lets me plot second plot, creates secondary y axis but it'll be same x axis.
ax2 = ax1.twinx()

# then plot the function using this twin axis
ax2.plot(x, h, 'r-', linewidth=2, label="h(x) = x³")
ax2.set_ylabel("h(x) = x³", color="red")

# some general plot related visual settings
plt.legend() 
plt.grid(True)
plt.title("Histogram and function")

# initial attempt looked really misaligned so
# copied this from principles of DA notes where i had to make a few histograms and they were all overlapping
# see: https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide.
fig.tight_layout()

# save as png to show Andrew
# see: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html 
plt.savefig('plottask.png')

#show the plot
plt.show()
