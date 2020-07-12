import cv2    
import numpy as np
from PIL import ImageGrab
import random
import time
import pynput.mouse
import pynput.keyboard
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

a = open('names.txt','r').read()
b = open('qtd.txt','r').read()
c = open('listacompleta.txt','a')
l1=a.split('\n')
l2=b.split('\n')
for i in range(len(l1)):
 mouse.position=(1317,274)
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
 time.sleep(0.3+0.1*random.random())
 keyboard.type(l1[i])
 time.sleep(1+0.1*random.random())
 print(int(l2[i]))
 for j in range (int(l2[i])):
  print(l1[i])
  time.sleep(0.8)
  mouse.position=(1855,415)
  mouse.press(pynput.mouse.Button.left)
  mouse.release(pynput.mouse.Button.left)