#! /usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import wavepy as wv

def main():
    name='db6'
    [lp1,hp1,lp2,hp2]=wv.filter.filtcoef(name)
    length=len(lp1)
    x=np.arange(length)
    ymin=np.zeros(length)
    plt.subplot(2,2,1)
    plt.vlines(x,ymin,lp1)
    plt.xlabel('Low Pass 1')
    plt.subplot(2,2,2)
    plt.vlines(x,ymin,hp1)
    plt.xlabel('High Pass 1')
    plt.subplot(2,2,3)
    plt.vlines(x,ymin,lp2)
    plt.xlabel('Low Pass 2')
    plt.subplot(2,2,4)
    plt.vlines(x,ymin,hp2)
    plt.xlabel('High Pass 2')
    plt.show()
    
if __name__ == '__main__':
    main()       
    
    