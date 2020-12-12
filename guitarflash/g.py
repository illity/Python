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
  rect= {"left": 870, "top": 720, "width": 150, "height": 10}
  sct_img = sct.grab(rect)
  return Image.frombytes('RGB',sct_img.size, sct_img.bgra,'raw','BGRX')

keys=['','','','','','','','','','','','','','','','','','','','','','',
      '','','','','','','','','','','','','','','','','','','','','','',
]

maximo=0
b=0
while(1):
 tempo=time.time()
 img2=np.array(capture())
 img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 key=''
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
 b+=1
 key=''
 if b%4==0:
  if 'a' in keys[0] or 'a' in keys[1]:
   key+='a'
  if 's' in keys[0] or 's' in keys[1]:
   key+='s'
  if 'j' in keys[0] or 'j' in keys[1]:
   key+='j'
  if 'k' in keys[0] or 'k' in keys[1]:
   key+='k'
  if 'l' in keys[0] or 'l' in keys[1]:
   key+='l'
  if key!='' and key!='asjkl':
   keyboard.type(key)
 keys.pop(0)
 #10 erradas 5 perdidas
 #print(keys)