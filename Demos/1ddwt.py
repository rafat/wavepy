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
	J=3
	nm='db5'
	ext='per'
	input=open('pieceregular2048.txt','r')
	for file in input:
		x=np.append(x,float(file))
	
	input.close()
	[dwtop,length,flag]=wv.dwt.dwt(x,J,nm,ext)
	
	fig1=plt.figure()	
	plt.suptitle('DWT Decomposition')
	plt.suptitle('DWT Decomposition')
	plt.subplot(J+2,1,1)
	plt.plot(x)
	plt.ylabel('Orig Sig')
	plt.subplot(J+2,1,2)
	s='{0}{1}'.format('Appx J=',J)
	plt.ylabel(s)
	plt.plot(dwtop[0:length[0]])
	iter=int(length[0])
	
	for i in range(J):
		val=int(length[i+1])
		oup=dwtop[iter:iter+val]
		iter+=val
		plt.subplot(J+2,1,i+3)
		n=int(J-i)
		s='{0}{1}'.format('Detail J=',n)
		plt.ylabel(s)
		plt.plot(oup)
	plt.draw()
	
	fig2=plt.figure()
	plt.title('Reconstructed Signal')
	idwtop=wv.dwt.idwt(dwtop,nm,length,flag)
	plt.plot(idwtop)
	plt.draw()
	
	plt.show()
		
	

if __name__ == '__main__':
	main()    

