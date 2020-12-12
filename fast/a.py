from PIL import ImageGrab
import numpy as np
import cv2
import pynput.mouse
import time
from ctypes import *
user=windll.LoadLibrary('c:\\windows\\system32\\user32.dll')
h=user.GetDC(0)
gdi=windll.LoadLibrary('c:\\windows\\system32\\gdi32.dll')
iter=0
for j in range(20):
 for i in range(5):
  pynput.mouse.Controller().position=(960,600)
  pynput.mouse.Controller().click(pynput.mouse.Button.left)
  time.sleep(0.2)
  pixel=gdi.GetPixel(h,250,250)
  while(1):
   if gdi.GetPixel(h,250,250)!=pixel:
    pynput.mouse.Controller().click(pynput.mouse.Button.left)
    break
  time.sleep(0.2)
 cv2.imwrite('{}.png'.format(iter),cv2.cvtColor(np.array(ImageGrab.grab()),cv2.COLOR_BGR2RGB))
 iter+=1
 pynput.mouse.Controller().position=(1025,580)
 pynput.mouse.Controller().click(pynput.mouse.Button.left)
 time.sleep(0.3)
