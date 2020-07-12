import numpy as np
import cv2
from math import sin,cos
from operator import itemgetter

def line(img,st,th):
 p=0
 while (st[0]+p*sin(th)<img.shape[0] and st[1]+p*cos(th)<img.shape[1]):
  img[st[0]+int(p*sin(th)),st[1]+int(p*cos(th))]=255
  p=p+1
 return img


def linechk(img,st,th):
 p=0
 soma=0
 while (st[0]+p*sin(th)<img.shape[0] and st[1]+p*cos(th)<img.shape[1] and st[0]+p*sin(th)>=0 and st[1]+p*cos(th)>=0):
  #print(st[0]+p*sin(th))
  soma+=img[st[0]+int(p*sin(th)),st[1]+int(p*cos(th))][0]**2+img[st[0]+int(p*sin(th)),st[1]+int(p*cos(th))][1]**2+img[st[0]+int(p*sin(th)),st[1]+int(p*cos(th))][2]**2
  p=p+1
 return soma

img = cv2.imread('a.jpg')
img = cv2.resize(img, (img.shape[1]//4, img.shape[0]//4),interpolation = cv2.INTER_AREA)
img2 = np.zeros((img.shape[0], img.shape[1]))
for i in range(200,300,20):
 for j in range(100, 300, 20):
  best=[]
  for th in range(1,20):
   best.append(linechk(img,(i, j),3.14*th/20))
  idx=max(enumerate(best), key=itemgetter(1))[0] 
  img=line(img,(i,j),3.14*idx/20)
  img2=line(img2,(i,j),3.14*idx/20)
  cv2.imshow('1',img)
  cv2.imshow('',img2)
  cv2.waitKey(1)
  print(idx)