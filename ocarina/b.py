import cv2
import numpy as np

tablatura = 'f1 e1 d1 c1 d1 d1 a1 e1 e1 d1 c1'
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
completar = np.zeros((320,400*(4-i%5),3))
line = np.concatenate((line,completar), axis=1)
full = np.concatenate((full,line), axis=0)
cv2.imshow('full',full); cv2.waitKey()
cv2.imwrite(tablatura+'.png',full)