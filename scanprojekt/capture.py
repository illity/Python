import cv2
import numpy as np
from PIL import ImageGrab
import pynput.mouse
mouse = pynput.mouse.Controller()

img_bgr = np.array(ImageGrab.grab(bbox=(696,279,726,314)))
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
while(1): print('{}'.format(mouse.position))
#696,279
#726,314
cv2.imwrite('template5.png',img_gray)
cv2.waitKey()
cv2.destroyAllWindows()
675,250
925,725