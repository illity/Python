import cv2
import numpy as np
from PIL import ImageGrab
import time
#img=np.array(ImageGrab.grab(bbox=(863,720,1033,740)))
#img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
import pynput.keyboard
keyboard = pynput.keyboard.Controller()
keys=['','','','','','','','','']
maximo=0
while(1):
 tempo=time.time()
 img2=np.array(ImageGrab.grab(bbox=(870,720,1020,732)))
 img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 #cv2.imshow('',img2)
 #cv2.waitKey(1)
 key=''
 #print(time.time()-tempo)
 #print(n)
 if 10 in np.where(img2==255)[1]:
  key=key+'a'
 if 43 in np.where(img2==255)[1]:
  key=key+'s'
 if 77 in np.where(img2==255)[1]:
  key=key+'j'
 if 115 in np.where(img2==255)[1]:
  key=key+'k'
 if 147 in np.where(img2==255)[1]:
  key=key+'l'
 keys=keys+[key]
 if keys[0]!='' and keys[0]!='asjkl':
  keyboard.type(keys[0])
 keys.pop(0)
 while time.time()-tempo<0.09:
  pass
 #10 erradas 5 perdidas
 #print(keys)