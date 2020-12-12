import pynput.mouse
import pynput.keyboard
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
from pynput.keyboard import Key, Listener
import time

def um():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0],inicial[1]+50)
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def dois():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+1,inicial[1]+1)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 time.sleep(0.5)
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def tres():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+1,inicial[1]+1)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+50)
 time.sleep(0.5)
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def quatro():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0],inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def cinco():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+50)
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def seis():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+25)
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def sete():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def oito():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def nove():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+25)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1])
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def zero():
 inicial=mouse.position
 mouse.press(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+30,inicial[1])
 time.sleep(0.5)
 mouse.position=(inicial[0]+30,inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1]+50)
 time.sleep(0.5)
 mouse.position=(inicial[0],inicial[1])
 mouse.release(pynput.mouse.Button.left)
 mouse.position=(inicial[0]+40,inicial[1])

def on_press(key):
    if (eval('{}'.format(key))=='0'):
     zero()
    if (eval('{}'.format(key))=='1'):
     um()
    if (eval('{}'.format(key))=='2'):
     dois()
    if (eval('{}'.format(key))=='3'):
     tres()
    if (eval('{}'.format(key))=='4'):
     quatro()
    if (eval('{}'.format(key))=='5'):
     cinco()
    if (eval('{}'.format(key))=='6'):
     seis()
    if (eval('{}'.format(key))=='7'):
     sete()
    if (eval('{}'.format(key))=='8'):
     oito()
    if (eval('{}'.format(key))=='9'):
     nove()

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
print(mouse.position)