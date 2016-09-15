#!bin/usr/env python

import numpy as np
import matplotlib.pyplot as plt

"""Makes a plot of the function y(t)=v_0*t - (1/2)gt^2 for v_0, g, and a 
range of t; plot is height vs time. It also includes a function that 
reads a set of values for v_0 from the command line and plots each curve 
on the same figure. """

def f(t, v):
    return (v*t - (1.0/2.0)*9.81*(t**2))



def getVTY():
"""Takes user input for v, creates arrays for t and the resulting f(t,v)."""
    v = [int(i) for i in raw_input("Enter your list of v_0's, separated by commas: ").split(",")]
    np.asarray(v)
    t = np.linspace(0, v/9.81, 40)
    vf = np.vectorize(f)
    y = vf(t, v)

def plot1(t, y, v):
    plt.plot(t, y)
    plt.xlabel('t')
    plt.ylabel('h')
    plt.axis([0.0, v/9.81, 0.0, np.amax(y)+3])
    plt.savefig('y(t).pdf')
    plt.show()


