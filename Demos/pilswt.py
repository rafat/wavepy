#! /usr/bin/env python

import numpy as np
import wavepy as wv
import Image

""" 
Dependencies
1.Numpy
2. PIL (Python Imaging Library)

This program only processes grayscale images.
    Use convert("L") to convert to grayscale
    To process color images, process each channel separately"""

def main():
    x=np.asarray(Image.open("empire.jpg").convert("L"))
    J=2
    nm='bior3.3'
    [swtop,length]=wv.dwt.swt2(x,J,nm)
    
    row=length[0]
    col=length[1]
    
    blur=swtop[0:row*col]
    blur=np.reshape(blur,[row,col])
    blur[blur<0.0]=0.0
    blur=blur*255.0/blur.max()
    blur[blur>255.0]=255.0
    Image.fromarray(np.uint8(blur)).show()
    
    
    detail=swtop[row*col:]
    detail=np.reshape(detail,[row*J*3,col])
    
    detail[detail<0.0]=0.0
    Image.fromarray(np.uint8(detail)).show()
    


if __name__ == '__main__':
    main()    