import cv2
import numpy as np

tablatura = 'f e d c d d a e e d c'
notas = tablatura.split(' ')
for i in range(len(notas)):
 if not (i%5):
  print('src/'+notas[i]+'.png')
  if i==5:
   full = np.copy(line)
  if i!=0 and i>5:
   full = np.concatenate((full,line), axis=0)
   #cv2.imshow('',full); cv2.waitKey()
  line = cv2.imread('src/'+notas[i]+'.png')
 else:
  print('oi')
  line = np.concatenate((line,cv2.imread('src/'+notas[i]+'.png')), axis=1)
 cv2.imshow('',line); cv2.waitKey()
completar = np.zeros((248,127*(4-i%5),3))
line = np.concatenate((line,completar), axis=1)
full = np.concatenate((full,line), axis=0)
cv2.imshow('full',full); cv2.waitKey()
cv2.imwrite(tablatura+'.png',full)