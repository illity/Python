import numpy as np
import cv2
def t2i():
 a=open('c.py','rb').read()
 sz=(int((len(a)/3)**0.5+1),int((len(a)/3)**0.5+1),3)
 #print(sz)
 img=np.zeros(sz,dtype=np.uint8)
 for i in range(len(a)):
  #print(int(i/(3*sz[1])),int(i/3)%sz[1],i%3)
  img[int(i/(3*sz[1])),int(i/3)%sz[1],i%3]=a[i]
 cv2.imwrite('img.png',img)
def i2t():
 img2=cv2.imread('img.png')
 sz=img2.shape
 #print(img2)
 #print(img2.reshape(27))
 text=''
 for i in img2.reshape(sz[0]*sz[1]*sz[2]): text=text+chr(i)
 print(text)
 #print(img)

t2i()
i2t()