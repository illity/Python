import cv2
import sys
import numpy as np

disks = 10

def disp(hanoi):
 img=np.zeros((2*disks,1,3), np.uint8)
 for h in hanoi:
  tower=np.zeros((2*disks,2*disks,3),np.uint8)
  for i in range(2*disks-1):
   tower[2*disks-i-1,disks-1]=(0,0,255); tower[2*disks-i-1,disks]=(0,0,255)
  for i in range(len(h)):
   tower[2*disks-2*i-1,disks-h[i]:disks+h[i],...]=255
  img=np.concatenate((img,tower),axis=1)
  img=np.concatenate((img,np.zeros((2*disks,1,3),np.uint8)),axis=1)
 img=cv2.resize(img, (20*disks+10,20*disks), interpolation=cv2.INTER_AREA)
 video.append(img)
 cv2.imshow('',img)
 cv2.waitKey(1)
 #cv2.destroyAllWindows()
 return 1

def permanentdisp(hanoi):
 img=np.zeros((2*disks,1,3), np.uint8)
 for h in hanoi:
  tower=np.zeros((2*disks,2*disks,3),np.uint8)
  for i in range(2*disks-1):
   tower[2*disks-i-1,disks-1]=(0,0,255); tower[2*disks-i-1,disks]=(0,0,255)
  for i in range(len(h)):
   tower[2*disks-2*i-1,disks-h[i]:disks+h[i],...]=255
  img=np.concatenate((img,tower),axis=1)
  img=np.concatenate((img,np.zeros((2*disks,1,3),np.uint8)),axis=1)
 img=cv2.resize(img, (20*disks+10,20*disks), interpolation=cv2.INTER_AREA)
 cv2.imshow('',img)
 cv2.waitKey()
 #cv2.destroyAllWindows()

def mov(hanoi, t1, t2):
 hanoi[t2].append(hanoi[t1][len(hanoi[t1])-1])
 hanoi[t1].pop(len(hanoi[t1])-1)
 return 1

def notx(t1,t2):
 return (3-(t1+t2))

def solve(hanoi, t1, t2, el):
 if el!=1:
  solve(hanoi, t1, notx(t1,t2), el-1)+mov(hanoi, t1, t2)+disp(hanoi)+solve(hanoi, notx(t1,t2), t2, el-1)
  return 1
 if el==1:
  mov(hanoi, t1, t2)+disp(hanoi)
  return 1

video = []
hanoi = [[] for i in range(3)]
hanoi[0] = [disks-i for i in range(disks)]
solve(hanoi, 0, 1, disks)
permanentdisp(hanoi)
writer = cv2.VideoWriter("output2.mp4", cv2.VideoWriter_fourcc(*"xvid"), 30,(20*disks+10,20*disks))
for i in range(2**disks-1):
 writer.write(video[i])
writer.release()
print('oi')
cv2.destroyAllWindows()