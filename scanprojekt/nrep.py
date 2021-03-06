import cv2    
import numpy as np
from PIL import ImageGrab
import random
import time
import pynput.mouse
import pynput.keyboard
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()


def find():
    count=0
    threshold=0.999
    img_bgr = np.array(ImageGrab.grab(bbox=(625,250,925,725)))
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('template.png',cv2.IMREAD_GRAYSCALE)
    w1,h1=template.shape[::-1]
    
    result=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    
    loc=np.where(result>=threshold)

    for pt1 in zip(*loc[::-1]):
        cv2.rectangle(img_bgr,pt1,(pt1[0]+w1,pt1[1]+h1),(0,255,0),2)
        count=count+1
    #cv2.imshow("image",img_bgr)
    #cv2.imwrite('res.png',img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return count

while 1: print(mouse.position)
lista = open('lista.txt','r').read()
for x in lista.split('\n'):
 print(x)
 mouse.position=(830,500)
 mouse.press(pynput.mouse.Button.left)
 mouse.release(pynput.mouse.Button.left)
 mouse.press(pynput.mouse.Button.left)
 mouse.release(pynput.mouse.Button.left)
 mouse.press(pynput.mouse.Button.left)
 mouse.release(pynput.mouse.Button.left)
 time.sleep(0.1+0.1*random.random())
 keyboard.type(x)
 time.sleep(1+0.1*random.random())
 mouse.position=(800,200)
 mouse.press(pynput.mouse.Button.left)
 mouse.release(pynput.mouse.Button.left)
 mouse.press(pynput.mouse.Button.left)
 mouse.release(pynput.mouse.Button.left)
 