import cv2
import numpy as np
from PIL import ImageGrab, Image
import time
from mss import mss
#img=np.array(ImageGrab.grab(bbox=(863,720,1033,740)))
#img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
import pynput.keyboard
keyboard = pynput.keyboard.Controller()

def capture(x):
 with mss() as sct:
  monitor=sct.monitors[1]
  rect= {"left": x, "top": 720, "width": 1, "height": 12}
  sct_img = sct.grab(rect)
  return Image.frombytes('RGB',sct_img.size, sct_img.bgra,'raw','BGRX')


keys=['','','',''
]

maximo=0
b=0
while(1):
 tempo=time.time()
 key=''
 #print(np.array(capture(880)))
 #print(np.where(cv2.cvtColor(np.array(capture(880)),cv2.COLOR_BGR2GRAY)==255))
 if [255] in cv2.cvtColor(np.array(capture(880)),cv2.COLOR_BGR2GRAY)[1]:
  key=key+'a'
 if [255] in cv2.cvtColor(np.array(capture(913)),cv2.COLOR_BGR2GRAY)[1]:
  key=key+'s'
 if [255] in cv2.cvtColor(np.array(capture(947)),cv2.COLOR_BGR2GRAY)[1]:
  key=key+'j'
 if [255] in cv2.cvtColor(np.array(capture(985)),cv2.COLOR_BGR2GRAY)[1]:
  key=key+'k'
 if [255] in cv2.cvtColor(np.array(capture(1017)),cv2.COLOR_BGR2GRAY)[1]:
  key=key+'l'
 keys=keys+[key]
 b+=1
 key=''
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