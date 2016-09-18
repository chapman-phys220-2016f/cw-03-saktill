#! bin/usr/env python

import urllib2
import matplotlib.pyplot as plt
import numpy as np

"""The purpose of this module is to read a specific file (src/plot/xy.dat),
which contains two columns of numbers, one for x values and one for y values.
This module contains a function to do that, which puts them into lists, and
a function which will plot the curve, and a function to calculate the mean y
value, as well as the max and min of y."""

def getData():
    """Pulls data from a github file /scipro-primer/master/src/plot/xy.dat
    and formats it into a list of x coordinates and a list of y coord."""
    fullFile = urllib2.urlopen('https://raw.githubusercontent.com/hplgit/scipro-primer/master/src/plot/xy.dat')
    x = []
    y = []
    for line in fullFile:
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))
    return y, x

def plotData(x, y):
    """creates plot of x vs y"""
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('X vs Y')

def yData(y):
    """returns mean, max, and min of the y values"""
    one = 0
    for i in y:
        one += i
    yMean = one/float(len(y))
    yMax = np.amax(y)
    yMin = np.amin(y)
    return yMean, yMax, yMin

