import sys
import time
import shutil
import os
f = open('{}'.format(sys.argv[1]),'rb')
a=time.time()
c=[int(i) for i in sys.argv[2].strip('][').split(', ')]
print(c)
i=0
ten=[]
raw=f.read()
outname=''
m=[]
for i in range(100):
 m.append(i*os.path.getsize(sys.argv[1])//100)
i=0
for ch in sys.argv[1]:
 x=ch
 if ord(ch)>64 and ord(ch)<91:
  x=chr((ord(x)-65+c[i%(len(c))])%26+65)
 if ord(ch)>96 and ord(ch)<123:
  x=chr((ord(x)-97+c[i%(len(c))])%26+97)
 if ord(ch)>47 and ord(ch)<58:
  x=chr((ord(x)-48+c[i%(len(c))])%10+48)
 outname=outname+x
 i=i+1
print(outname)
i=0
for p in m:
 f.seek(p)
 j=0
 for b in f.read():
  ten.append((b+c[i%(len(c))])%256)
  j=j+1
  if j==100: break
 i=i+1
f.close()
shutil.copy('{}'.format(sys.argv[1]),outname)
out = open('{}'.format(outname),'r+b')
i=0
for p in m:
 out.seek(p)
 out.write(bytes(ten[i*100:100+i*100]))
 i=i+1
print('time ellapsed: '+str(time.time()-a))