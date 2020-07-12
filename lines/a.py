import numpy as np
import cv2
from math import sin,cos

def line(img,i,th):
 p=0
 while (p*sin(th)<img.shape[1] and p*cos(th)<img.shape[0]):
  img[int(p*sin(th)),int(p*cos(th))]=255
  cv2.imshow('',img)
  cv2.waitKey(1)
  p=p+1
 return img

img = np.zeros((100,100))
for st in range(1):
 img=line(img,0,45)