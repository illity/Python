import cv2
import numpy as np
from PIL import ImageGrab
import time
img=np.array(ImageGrab.grab(bbox=(750,854,1150,868)))
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
import pynput.keyboard
keyboard = pynput.keyboard.Controller()
keys=['','','','']
while(1):
 img2=np.array(ImageGrab.grab(bbox=(750,854,1150,868)))
 img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 #cv2.imshow('',img2)
 #cv2.imwrite('a.png',img2)
 #cv2.waitKey(1)
 key=''
 #print(n)
 if 69 in np.where(img2==255)[1]:
  key=key+'a'
 if 132 in np.where(img2==255)[1]:
  key=key+'s'
 if 197 in np.where(img2==255)[1]:
  key=key+'j'
 if 266 in np.where(img2==255)[1]:
  key=key+'k'
 if 329 in np.where(img2==255)[1]:
  key=key+'l'
 keys=keys+[key]
 if keys[0]!='asjkl':
  keyboard.type(keys[0])
 keys.pop(0)
 print(keys)