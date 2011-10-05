#! /usr/bin/env python

""" Dependencies
1. Numpy
2. matplotlib"""

import numpy as np
import wavepy as wv
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    a=np.ones(8)
    b=wv.convol.convol(a,a)
    c=np.real(wv.convol.convfft(b,a))
       
    
    plt.subplot(3,1,1)
    plt.plot(a)
    plt.ylabel('A')
    
    plt.subplot(3,1,2)
    plt.plot(b)
    plt.ylabel('B=conv(A,A)')
    
    plt.subplot(3,1,3)
    plt.plot(c)
    plt.ylabel('C=conv(A,B)')
    
    
    plt.show()
    
if __name__ == '__main__':
    main()     
    