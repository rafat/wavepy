#! /usr/bin/env python

"""Dependencies
1.Numpy
2. PIL (Python Imaging Library)"""

import numpy as np
import wavepy as wv
import Image

""" This program only processes grayscale images.
    Use convert("L") to convert to grayscale
    To process color images, process each channel separately"""

def main():
    x=np.asarray(Image.open("empire.jpg").convert("L"))
    J=3
    nm='db3'
    ext='sym'
    [dwtop,length,flag]=wv.dwt.dwt2(x,J,nm,ext)
    disp=wv.dwt.dispdwt(dwtop,length,J)
    length2=wv.dwt.out_dim(length,J)
    l0=length2[0]
    l1=length2[1]
    disp[disp<0.0]=0.0
    
    disp[0:l0,0:l1]=disp[0:l0,0:l1]*255.0/disp.max()
    disp[disp>255.0]=255.0
    Image.fromarray(np.uint8(disp)).show()
    """plt.imshow(disp,cmap=cm.gray)
    plt.show()"""
    """oup=wv.dwt.idwt2(dwtop,nm,length,flag)
    plt.imshow(oup,cmap=cm.gray)
    plt.show()"""
    
    oup=wv.dwt.idwt2(dwtop,nm,length,flag)
    Image.fromarray(np.uint8(oup)).show()
    
    
    
if __name__ == '__main__':
    main()    

