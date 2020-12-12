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
  rect= {"left": 880, "top": 720, "width": 138, "height": 10}
  sct_img = sct.grab(rect)
  return Image.frombytes('RGB',sct_img.size, sct_img.bgra,'raw','BGRX')

def capture2():
 with mss() as sct:
  monitor=sct.monitors[1]
  rect= {"left": 880, "top": 677, "width": 130, "height": 10}
  sct_img = sct.grab(rect)
  return Image.frombytes('RGB',sct_img.size, sct_img.bgra,'raw','BGRX')
#16,43,67,91,117

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
 if 0 in np.where(img2==255)[1]:
  key=key+'a'
 if 33 in np.where(img2==255)[1]:
  key=key+'s'
 if 67 in np.where(img2==255)[1]:
  key=key+'j'
 if 105 in np.where(img2==255)[1]:
  key=key+'k'
 if 137 in np.where(img2==255)[1]:
  key=key+'l'
 keys=keys+[key]
 b+=1
 key=''
 if b%4==0:
  if ('a' in keys[0]) * ('a' in keys[1]) + ('a' in keys[1]) * ('a' in keys[2]) :
   key+='a'
  if ('s' in keys[0]) * ('s' in keys[1]) + ('s' in keys[1]) * ('s' in keys[2])  :
   key+='s'
  if ('j' in keys[0]) * ('j' in keys[1]) + ('j' in keys[1]) * ('j' in keys[2]) :
   key+='j'
  if ('k' in keys[0]) * ('k' in keys[1]) + ('k' in keys[1]) * ('k' in keys[2])  :
   key+='k'
  if ('l' in keys[0]) * ('l' in keys[1]) + ('l' in keys[1]) * ('l' in keys[2])  :
   key+='l'
  if key!='' and key!='asjkl':
   keyboard.type(key)
 keys.pop(0)
 #10 erradas 5 perdidas
 #print(keys)