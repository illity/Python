from mss import mss
from PIL import Image,ImageGrab
import numpy as np
import cv2
import time
def capture():
 with mss() as sct:
  monitor=sct.monitors[1]
  rect= {"left": 870, "top": 720, "width": 150, "height": 12}
  sct_img = sct.grab(rect)
  return Image.frombytes('RGB',sct_img.size, sct_img.bgra,'raw','BGRX')
tmp=time.time()
for i in range(50):
 img=np.array(capture())
 #img=ImageGrab.grab()
print((time.time()-tmp)/50)
cv2.imshow('',np.array(img))
cv2.waitKey()