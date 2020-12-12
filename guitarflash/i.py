import cv2
import numpy as np
from PIL import ImageGrab, Image
import time
from mss import mss
#img=np.array(ImageGrab.grab(bbox=(863,720,1033,740)))
#img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
import pynput.keyboard
keyboard = pynput.keyboard.Controller()

def capture():
 with mss() as sct:
  monitor=sct.monitors[1]
  rect= {"left": 900, "top": 658, "width": 94, "height": 7}
  sct_img = sct.grab(rect)
  return Image.frombytes('RGB',sct_img.size, sct_img.bgra,'raw','BGRX')

keys=['','','','','','','','','','','','','','','','','','','','','',
      '','','','','','','','','','','','','','','','','','','','','',
      '','','','','','','','','','','','','','','','','','','','','',
      '','','','','','','','','','','','','','','','','']
maximo=0
b=0
while(1):
 tempo=time.time()
 img2=np.array(capture())
 img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 #cv2.imshow('',img2)
 #cv2.waitKey(1)
 key=''
 #print(time.time()-tempo)
 #print(n)
 if(np.where(img2==255)[1].size>0): cv2.imwrite('100.png',img2)
 if 6 in np.where(img2==255)[1]:
  key=key+'a'
 if 27 in np.where(img2==255)[1]:
  key=key+'s'
 if 47 in np.where(img2==255)[1]:
  key=key+'j'
 if 70 in np.where(img2==255)[1]:
  key=key+'k'
 if 90 in np.where(img2==255)[1]:
  key=key+'l'
 keys=keys+[key]
 b+=1
 key=''
 if b%6==0:
  if 'a' in keys[0] or 'a' in keys[1] or 'a' in keys[2] or 'a' in keys[3]:
   key+='a'
  if 's' in keys[0] or 's' in keys[1] or 's' in keys[2] or 's' in keys[3]:
   key+='s'
  if 'j' in keys[0] or 'j' in keys[1] or 'j' in keys[2] or 'j' in keys[3]:
   key+='j'
  if 'k' in keys[0] or 'k' in keys[1] or 'k' in keys[2] or 'k' in keys[3]:
   key+='k'
  if 'l' in keys[0] or 'l' in keys[1] or 'l' in keys[2] or 'l' in keys[3]:
   key+='l'
  if key!='' and key!='asjkl':
   keyboard.type(key)
 keys.pop(0)
 #10 erradas 5 perdidas
 #print(keys)