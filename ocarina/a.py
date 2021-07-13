import cv2
import numpy as np

img = cv2.imread('a.png')
cv2.imshow('',img); cv2.waitKey()
sz = img.shape
names = ['a','b','c1','d1','e1','f1','g1','a1','b1','c2','d2','e2','f2','as','c1s','d1s','f1s','g1s','n','a1s','c2s','d2s','n']
for i in range(4):
 for j in range(6):
  print()
  if i<3:
   posx = [435*i,435*i+320]
  else:
   posx = [img.shape[0]-320,img.shape[0]]
  posy = [int(img.shape[1]*j/6),int(img.shape[1]*(j+1)/6)]
  cv2.imshow('',img[posx[0]:posx[1],posy[0]:posy[1],:]); cv2.waitKey()
  cv2.imwrite('src/'+names[i*6+j]+'.png',img[posx[0]:posx[1],posy[0]:posy[1],:])
