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
lista = open('listanov.txt','r').read()
l = lista.split('\n')
for null in l:
 print(null)
 time.sleep(0.03+0.02*random.random())
 mouse.release(pynput.mouse.Button.left)
 time.sleep(0.03+0.02*random.random())
 mouse.press(pynput.mouse.Button.left)
 time.sleep(0.03+0.02*random.random())
 mouse.release(pynput.mouse.Button.left)
 time.sleep(0.03+0.02*random.random())
 mouse.press(pynput.mouse.Button.left)
 time.sleep(0.03+0.02*random.random())
 mouse.release(pynput.mouse.Button.left)
 time.sleep(0.05+0.02*random.random())
 keyboard.type(null.split(' -')[0])
 time.sleep(1.5+0.1*random.random())
 mouse.position=(1600,120)
 mouse.press(pynput.mouse.Button.left)
 time.sleep(0.05+0.02*random.random())
 mouse.release(pynput.mouse.Button.left)
 time.sleep(0.05+0.02*random.random())
 mouse.press(pynput.mouse.Button.left)
 time.sleep(0.03+0.02*random.random())
 mouse.release(pynput.mouse.Button.left)
 time.sleep(0.03+0.02*random.random())
 time.sleep(0.3)