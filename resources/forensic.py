import cv2
import numpy as np

def adj(pos,el):
 for i in range(3):
  for j in range(3):
   if (el[0]-1+i,el[1]-1+j) in pos: return adj(pos,el)

def find(img):
 pos=[]
 whr=np.where(img==255)
 for i in range(len(whr[0])):
  if i%3==0: pos.append((whr[0][i],whr[1][i]))
 while(pos!=[]):
  first=pos[0]
  print(adj(pos,first))

img=cv2.imread('a.png')
imgx = cv2.threshold(img,128,255,cv2.THRESH_BINARY)[1]
img_gray = cv2.cvtColor(imgx, cv2.COLOR_BGR2GRAY)
find(imgx)
cv2.imshow('',imgx)
cv2.waitKey()