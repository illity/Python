import cv2
import numpy as np
from math import *

def graph(functions,limits,sz,p,**kwargs):
 colors=kwargs.get('colors',None)
 if colors is None:
  colors=[(255,255,255)]*len(functions)
 else:
  if len(colors)!=len(functions): colors=[(255,255,255)]*len(functions)
 img=kwargs.get('img',None)
 if img is None:
  img=np.zeros((sz[0],sz[1],3),dtype=np.uint8)
 for j in range(len(functions)):
  xplot=[]
  yplot=[]
  for i in range(p):
   ev=functions[j](limits[0]+i*(limits[2]-limits[0])/p) #aqui calcula o f() de todos os pontos
   xplot.append(limits[0]+i*(limits[2]-limits[0])/p)
   yplot.append(ev)
  for i in range(len(xplot)):
   #print(xplot[i],yplot[i])
   if yplot[i]>=limits[1] and yplot[i]<=limits[3] and xplot[i]>=limits[0] and xplot[i]<=limits[2]:
    img[int(-1+(yplot[i]-limits[1])*(sz[1]-1)/(limits[1]-limits[3])),int((xplot[i]-limits[0])*(sz[0]-1)/(limits[2]-limits[0]))]=colors[j]
 return img

def plot(x,y,limits,sz,**kwargs):
 color=kwargs.get('color',None)
 if color is None:
  color=(0,0,255)
 img=kwargs.get('img',None)
 result=np.copy(img)
 if img is None:
  result=np.zeros((sz[1],sz[0],3),dtype=np.uint8)
 #desenhando os eixos
 axis=kwargs.get('axis',None)
 if axis is None: axis=1
 if axis==1:
  if 0>limits[0] and 0<limits[2]:
   result[:,int(-limits[0] * sz[0] // (limits[2] - limits[0])),:]=255
  if 0>limits[1] and 0<limits[3]:
   result[sz[1]+int(limits[1] * sz[1] // (limits[3] - limits[1])),:,:]=255
 div=5
 if axis==0: div=0
 for i in range(div):
  cv2.putText(result,'{}'.format(round(limits[0]+i*(limits[2]-limits[0])/div,3)), 
    (int((i*(limits[2]-limits[0])/div)*sz[0]//(limits[2]-limits[0])),sz[1]+int(limits[1] * sz[1] // (limits[3] - limits[1]))), 
    cv2.FONT_HERSHEY_SIMPLEX,
    0.4,
    (200,200,200),
    1)
  cv2.putText(result,'{}'.format(round(limits[1]+i*(limits[3]-limits[1])/div,3)), 
    (int(-limits[0] * sz[0] // (limits[2] - limits[0])),sz[1]-int((i*(limits[3]-limits[1])/div)*sz[1])//(limits[3]-limits[1])), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    0.4,
    (200,200,200),
    1)#
 #desenhando os pontos
 for i in range(len(x)-1):
  if y[i]>limits[1] and y[i]<limits[3] and x[i]>limits[0] and x[i]<limits[2]:
   result=cv2.line(result,
        (int((x[i]-limits[0]) * sz[0] / (limits[2] - limits[0]))-1,int(sz[1] - (y[i]-limits[1]) * sz[1] / (limits[3] - limits[1]))-1),
        (int((x[i+1]-limits[0]) * sz[0] / (limits[2] - limits[0]))-1,int(sz[1] - (y[i+1]-limits[1]) * sz[1] / (limits[3] - limits[1]))-1),
        color)
   #img[int(sz[1] - (y[i]-limits[1]) * sz[1] / (limits[3] - limits[1]))-1,int((x[i]-limits[0]) * sz[0] / (limits[2] - limits[0]))-1]=color
   
 #
 return result

def integrate(f,a,b):
 soma=0
 for i in range(10000):
  soma+=f(a+i*(b-a)/10000)*(b-a)/10000
 return soma

def integrate(f,w,a,b,**kwargs):
 p=kwargs.get('p',None)
 if p is None:
  p=10000
 soma=0
 for i in range(p):
  soma+=f(a+i*(b-a)/p,w)*(b-a)/p
 return soma

def function(x):
 return sin(x)+cos(x)
def function2(x):
 return sin(x)
def function3(x):
 return cos(x)


#image=np.zeros((500,500,3),dtype=np.uint8)
#for t in range(100):
# image=graph([function,function2,function3],[-pi+t/10,-2,pi+t/10,2],[500,500],20000,colors=[(255,0,0),(0,255,0),(255,255,255)])
# cv2.imshow('',image)
# cv2.waitKey(10)