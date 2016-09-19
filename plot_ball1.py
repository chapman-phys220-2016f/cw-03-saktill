#! bin/usr/env python

import numpy as np
import matplotlib.pyplot as plt

"""Makes a plot of the function y(t)=v_0*t - (1/2)gt^2 for v_0, g, and a 
range of t; plot is height vs time. It also includes a function that 
reads a set of values for v_0 from the command line and plots each curve 
on the same figure. """

def f(t, v):
    return (v*t - (1.0/2.0)*9.81*(t**2))

def getVTY():
    """Takes user input for v, and creates arrays for t and the resulting 
    f(t,v). So for each i, v[i], t[i], y[i] will be an initial value,
    an array of 100 times, and an array of 100 data points (y values).
    This function returns a list l = [v, t, y]."""
    #creates an array for v based on user input, split at the comma
    
    v = np.array([float(i) for i in raw_input("Enter your list of v_0's, separated by commas: ").split(",")])
    
    #creates an array of arrays, where each elemental array is a set of t's
    #corresponding to the set of y's for the SAME v_0
    t= np.array([np.linspace(0, float(i)/9.81, 100) for i in v])

    #creates array of arrays, where each elemental array is defined like:
    #y[i]=vf(t[i], v)
    vf = np.vectorize(f)
    y = np.asarray([vf(t[i], v[i]) for i in range(len(v))])
    return v, t, y

def plot1(v, t, y):
    """This function takes input in the form of v=array, t=array of arrays,
    y=array of arrays such that for each entry in v, t and y have a set of 
    data points. It will return a plot of those data points for each v_0,
    each plot on the same figure."""
    for i in xrange(len(v)):
        plt.plot(t[i], y[i])
        plt.hold('on')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Height vs time')
    plt.show()


