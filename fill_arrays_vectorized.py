#!/bin/bash/env python
import numpy as np


def main():
    """This function demonstrates vectorization of mathematical functions."""
    x = np.linspace(-4,4,41)
    y = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*(x**2))

    return y

if __name__ == "__main__":
    main()
