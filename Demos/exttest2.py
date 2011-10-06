#! /usr/bin/env python

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import wavepy as wv
from scipy import lena

def main():
    x=lena()
    
    a=int(32)
    
    y=wv.misc.per_ext2d(x,a)
    z=wv.misc.symm_ext2d(x,a)
    
    plt.subplot(2,1,1)
    plt.imshow(y,cmap=cm.gray)
    plt.xlabel('Periodic Ext')
    
    plt.subplot(2,1,2)
    plt.imshow(z,cmap=cm.gray)
    plt.xlabel('Symmetric Ext')
    
    plt.show()
    
if __name__ == '__main__':
    main()      