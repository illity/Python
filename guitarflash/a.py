import cv2
import numpy as np
from PIL import ImageGrab
import time
img=np.array(ImageGrab.grab(bbox=(750,864,1150,876)))
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
import pynput.keyboard
keyboard = pynput.keyboard.Controller()
keys=['','','','']
while(1):
 img2=np.array(ImageGrab.grab(bbox=(750,864,1150,876)))
 img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 #cv2.imshow('',img2)
 #cv2.imwrite('a.png',img2)
 #cv2.waitKey(1)
 n=img-img2
 key=''
 #print(n)
 if 60 in np.where(n!=0)[1]:
  key=key+'a'
 if 130 in np.where(n!=0)[1]:
  key=key+'s'
 if 200 in np.where(n!=0)[1]:
  key=key+'j'
 if 266 in np.where(n!=0)[1]:
  key=key+'k'
 if 330 in np.where(n!=0)[1]:
  key=key+'l'
 keys=keys+[key]
 keyboard.type(keys[0])
 keys.pop(0)
 print(keys)