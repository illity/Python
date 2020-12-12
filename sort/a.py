import cv2, numpy as np
sz=50
def show(a,b):
 img=np.zeros((4*sz,4*sz,3),dtype=np.uint8)
 for i in range(a.shape[0]):
  img[4*sz-4*a[i]:4*sz,4*i:4*i+3]=a[i]*255/10000
 img[4*sz-4*a[b]:4*sz,4*b:4*b+3,0]=255
 img[4*sz-4*a[b]:4*sz,4*b:4*b+3,0]=0
 img[4*sz-4*a[b]:4*sz,4*b:4*b+3,0]=255
 cv2.imshow('',img)
 cv2.waitKey()
def part(m,lo,hi):
 pivot=m[(hi+lo)//2]
 pos=(hi+lo)//2
 while lo<hi:
  while m[lo]<pivot: lo=lo+1
  while m[hi]>pivot: hi=hi-1
  aux=m[lo]
  m[lo]=m[hi]
  m[hi]=aux
 if (m[hi]!=pivot):
  m[pos]=m[hi]
  m[hi]=pivot
 return lo
#m=np.array([9,2,1,8,5,7,4,6,3])
#m=np.array([1, 2, 3, 4, 5, 7, 8, 6, 9])
m=np.random.randint(0,10000,(sz))
def quicksort(A,lo,hi):
 if lo<hi:
  p=part(m,lo,hi)
  quicksort(m,lo,p-1)
  quicksort(m,p+1,sz-1)
 return m
x=quicksort(m,0,sz-1)
show(m,sz//2)

#part(m,p+1,sz-1)