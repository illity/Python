from graph2 import *
import cv2

#writer = cv2.VideoWriter("gaara.mp4", cv2.VideoWriter_fourcc(*"xvid"), 30,(500,500))

raw=open('coordinates.md','r').read()
raw=raw.split(',')
xy=[[],[]]
for el in raw:
 el=(el.split('[')[1])
 el=(el.split(']')[0])
 if el[0]==' ': el=el[1:]
 el=el.replace(' ',',')
 el=el.replace(',,',',')
 el=el.replace(',,',',')
 el='('+el+')'
 el=el.replace('(,','(')
 open('gaara.md','a').write(el+'\n')
 xy[0].append(eval(el)[0])
 xy[1].append(eval(el)[1])
 #print(len(xy[0]))
 #cv2.imshow('',plot(xy[0],xy[1],[0,0,200,200],[500,500])); cv2.waitKey(1)
 #writer.write(plot(xy[0],xy[1],[0,0,200,200],[500,500]))
#writer.release()