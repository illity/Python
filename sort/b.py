import cv2, numpy as np
sz=5
def show(a,b):
 img=np.zeros((4*sz,4*sz,3),dtype=np.uint8)
 for i in range(a.shape[0]):
  img[4*sz-4*a[i]:4*sz,4*i:4*i+3]=a[i]*255/10000
 img[4*sz-4*a[b]:4*sz,4*b:4*b+3,0]=255
 img[4*sz-4*a[b]:4*sz,4*b:4*b+3,0]=0
 img[4*sz-4*a[b]:4*sz,4*b:4*b+3,0]=0
 cv2.imshow('',img)
 cv2.waitKey()
def quicksort(m,lo,hi):
 if m==[]: return []
 if len(m)==0: return m
 if len(m)==1: return m
 if len(m)==2: return [min(m),max(m)]
 if len(m)==3:
  for i in range(3):
   for j in range(i+1,3):
    if m[i]>m[j]:
     m[i]+=m[j]
     m[j]=m[i]-m[j]
     m[i]-=m[j]
  return m
 print(m)
 pivot=m[(hi+lo)//2]
 pos=(hi+lo)//2
 i=lo
 j=hi
 while(1):
  if j-i<=0: break
  while m[i]<pivot: i=i+1
  while m[j]>pivot: j=j-1
  aux=m[i]
  m[i]=m[j]
  m[j]=aux
  i=i+1
  j=j-1
 aux=i+1
 print(m[lo:aux])
 print(m[j-1:j])
 print(m[j:hi+1])
 return quicksort(m[lo:aux],0,aux-1)+m[j-1:j]+quicksort(m[j:hi+1],0,hi-j)
a=[9,2,1,8,5,7,4,6,3]
#quicksort(a,0,sz-1)
#quicksort([1,2,3],0,2)
print(quicksort(a,0,sz-1))
print(quicksort([3,2,1,4,5],0,4))
