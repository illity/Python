import cv2
import numpy as np

img = cv2.imread('c.png')
cv2.imshow('',img); cv2.waitKey()
sz = img.shape
names = ['Gp','Ap','Bb','B','C','Cs','D','Eb','E','F','Fs','G','Gs','A','Bbp','Bp','Cp','Cps','Dp','Ebp']
for i in range(2):
 for j in range(10):
  print()
  posx = [248*i,248*(i+1)]
  posy = [int(img.shape[1]*j/10),int(img.shape[1]*(j+1)/10)]
  cv2.imshow('',img[posx[0]:posx[1],posy[0]:posy[1],:]); cv2.waitKey()
  cv2.imwrite('src/'+names[i*10+j]+'.png',img[posx[0]:posx[1],posy[0]:posy[1],:])

#0:320
#430: