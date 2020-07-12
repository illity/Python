import cv2    
import numpy as np
from PIL import ImageGrab
import random
import time
import pynput.mouse
import pynput.keyboard
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

#while(1): print(mouse.position)
mouse.position=(85,285)
mouse.press(pynput.mouse.Button.left)
time.sleep(0.03+0.02*random.random())
mouse.release(pynput.mouse.Button.left)
time.sleep(0.07+0.03*random.random())
mouse.press(pynput.mouse.Button.left)
time.sleep(0.03+0.02*random.random())
mouse.release(pynput.mouse.Button.left)
time.sleep(0.07+0.03*random.random())
mouse.press(pynput.mouse.Button.left)
time.sleep(0.03+0.02*random.random())
mouse.release(pynput.mouse.Button.left)
time.sleep(0.3+0.01*random.random())
keyboard.type('coquille de submerge')
time.sleep(2)
mouse.position=(300,305)
time.sleep(0.1+0.01*random.random())
mouse.press(pynput.mouse.Button.left)
time.sleep(0.1+0.01*random.random())
mouse.release(pynput.mouse.Button.left)
time.sleep(1)
img_bgr = np.array(ImageGrab.grab(bbox=(375,325,675,437)))
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
cv2.imwrite('{}.png'.format(null),img_gray)