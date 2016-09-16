#!/bin/bash/env python
import numpy as np
import matplotlib.pyplot as plt


def main():
    y_0 = float(raw_input("Please enter the starting height of the ball: "))
    theta = float(raw_input("Please enter the starting angle you want your ball to be thrown at: "))
    v_0 = float(raw_input("Please enter your initial velocity: "))
    x = np.linspace(0,10,11)
    y = x*np.tan(theta) - (1.0/(2*(v_0**2)))*((9.8*(x**2))/np.cos(theta)**2) + y_0
    #print x
    #print y
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([0,10,0,100])
    plt.title('Kinematic ball trajectory')
    plt.show()
    


if __name__ == "__main__":

    main()
