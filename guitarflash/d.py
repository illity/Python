import cv2
import numpy as np
from PIL import ImageGrab
import time
#img=np.array(ImageGrab.grab(bbox=(863,720,1033,740)))
#img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
import pynput.keyboard
keyboard = pynput.keyboard.Controller()
keys=['','','','','','','','','','']
cont=0
while(1):
 img2=np.array(ImageGrab.grab(bbox=(863,720,1033,730)))
 img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 #cv2.imshow('',img2)
 cont=cont+1
 cv2.imwrite('{cont}.png',img2)
 #cv2.waitKey(1)
 key=''
 #print(n)
 if 17 in np.where(img2==255)[1]:
  key=key+'a'
 if 51 in np.where(img2==255)[1]:
  key=key+'s'
 if 85 in np.where(img2==255)[1]:
  key=key+'j'
 if 119 in np.where(img2==255)[1]:
  key=key+'k'
 if 153 in np.where(img2==255)[1]:
  key=key+'l'
 keys=keys+[key]
 if keys[0]!='asjkl':
  keyboard.type(keys[0])
 keys.pop(0)
 print(keys)