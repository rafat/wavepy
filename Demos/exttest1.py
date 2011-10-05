#! /usr/bin/env python

""" Dependencies
1. Numpy
2. matplotlib"""

import numpy as np
import wavepy as wv
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    x=np.arange(64)
    a=int(16)
    
    y=wv.misc.per_ext(x,a)
    z=wv.misc.symm_ext(x,a)
    
    plt.subplot(3,1,1)
    plt.plot(x)
    plt.ylabel('Signal')
    
    plt.subplot(3,1,2)
    plt.plot(y)
    plt.ylabel('per_ext')
    
    plt.subplot(3,1,3)
    plt.plot(z)
    plt.ylabel('sym_ext')
    
    plt.show()
    
if __name__ == '__main__':
    main()  