#! /usr/bin/env python

""" Dependencies
1. Numpy
2. matplotlib"""

import numpy as np
import wavepy as wv
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    x=np.array([])
    J=2
    nm='sym4'
    input=open('noisybumps.txt','r')
    for file in input:
        x=np.append(x,float(file))
    
    input.close()
    [swtop,length]=wv.dwt.swt(x,J,nm)
    
    fig1=plt.figure()   
    plt.suptitle('DWT Decomposition')
    plt.suptitle('DWT Decomposition')
    plt.subplot(J+2,1,1)
    plt.plot(x)
    plt.ylabel('Orig Sig')
    plt.subplot(J+2,1,2)
    s='{0}{1}'.format('Appx J=',J)
    plt.ylabel(s)
    plt.plot(swtop[0:length])
    
    for i in range(J):
        oup=swtop[length*(i+1):length*(i+2)]
        plt.subplot(J+2,1,i+3)
        n=int(J-i)
        s='{0}{1}'.format('Detail J=',n)
        plt.ylabel(s)
        plt.plot(oup)
    plt.draw()
    
    fig2=plt.figure()
    plt.title('Reconstructed Signal')
    iswtop=wv.dwt.iswt(swtop,J,nm)
    plt.plot(iswtop)
    plt.draw()
    
    plt.show()
        
    

if __name__ == '__main__':
    main()    

