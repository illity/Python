import random
import cv2
import numpy as np
def show(a):
 img=np.zeros((4*sz,4*sz,3),dtype=np.uint8)
 for i in range(len(a)):
  img[4*sz-4*a[i]:4*sz,4*i:4*i+3]=5*a[i]
 cv2.imshow('',img)
 cv2.waitKey()
def swap(a,i,j):
 aux=a[i]
 a[i]=a[j]
 a[j]=aux
 return a
def quicksort(a,lo,hi):
 if len(a)<2: return a
 if len(a)==2: 
  return [min(a),max(a)]
 pivot=a[(len(a)//2)]
 while(1):
  i,j=lo,hi
  while a[i]<pivot: i+=1
  while a[j]>pivot: j-=1
  a=swap(a,i,j)
  if i==j:
   break
 #print(a[0:i],0,i-1)
 #print(a[i])
 #print(a[i+1:hi+1],0,hi-2)
 return quicksort(a[0:i],0,i-1)+a[i:i+1]+quicksort(a[i+1:hi+1],0,hi-i-1)
m = random.sample(range(50), 50)
sz=len(m)
print(m)
print(quicksort(m,0,len(m)-1))
show(quicksort(m,0,len(m)-1))