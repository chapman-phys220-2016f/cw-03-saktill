#!/bin/bash/env python
import numpy as np
import matplotlib.pyplot as plt


def main():
    y_0 = float(raw_input("Please enter the starting height of the ball: "))
    theta = float(raw_input("Please enter the starting angle you want your ball to be thrown at: "))
    v_0 = float(raw_input("Please enter your initial velocity: "))
    xMax = (2*(v_0)**2 * np.sin(theta)*np.cos(theta))/9.8
    x = np.linspace(0,xMax,100)
    y = x*np.tan(theta) - (1.0/(2*(v_0**2)))*((9.8*(x**2))/np.cos(theta)**2) + y_0
    
    #print x
    #print y
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Kinematic ball trajectory')
    plt.show()
    


if __name__ == "__main__":

    main()
