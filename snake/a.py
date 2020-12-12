import cv2, numpy as np, random
#moves->-2 = down -1 = left 1=right 2 up

def build():
 x=np.zeros((400,400,3), dtype=np.uint8)
 return x
def play(x,kobra,move,lemon):
 new=[kobra[0][0]-(int(move/2) if abs(move)>1 else 0),kobra[0][1]+(move if abs(move)<=1 else 0)]
 print(lemon)
 print(new)
 print(kobra)
 if new[0]==kobra[1][0] and new[1]==kobra[1][1]:
  kobra.reverse()
  #new=[kobra[0][0]-(int(move/2) if abs(move)>1 else 0),kobra[0][1]+(move if abs(move)<=1 else 0)]
  return [x,kobra,move,lemon]
 if new in kobra[:len(kobra)-1]: kobra=[[random.randint(0,24),random.randint(0,24)]]; kobra=kobra+[[kobra[0][0]+i+1,kobra[0][1]]]
 new[0]=24 if new[0]==-1 else 0 if new[0]==25 else new[0]
 new[1]=24 if new[1]==-1 else 0 if new[1]==25 else new[1]
 kobra=[new]+kobra
 if new!=lemon: kobra.pop()
 else:
  lemon=[random.randint(0,24),random.randint(0,24)]
  while(lemon in kobra): lemon=[random.randint(0,24),random.randint(0,24)]
 return [x,kobra,move,lemon]
kobra=[[random.randint(0,24),random.randint(0,24)]]
for i in range(1): kobra=kobra+[[kobra[0][0]+i+1,kobra[0][1]]]
move=1
lemon=[random.randint(0,24),random.randint(0,24)]
#writer = cv2.VideoWriter("output3.mp4", cv2.VideoWriter_fourcc(*"xvid"), 30,(400,400))
while(1):
 x=build()
 x,kobra,move,lemon=play(x,kobra,move,lemon)
 x[16*lemon[0]+1:16*lemon[0]+15,16*lemon[1]+1:16*lemon[1]+15]=(0,255,0)
 for pos in kobra:
  x[16*pos[0]+1:16*pos[0]+15,16*pos[1]+1:16*pos[1]+15]=255
 cv2.imshow('',x)
 print(len(kobra))
 #writer.write(x)
 k=cv2.waitKey(40)
 move=-2 if k==115 else -1 if k==97 else 1 if k==100 else 2 if k==119 else move
 if k==ord('p'): break
#writer.release()
cv2.destroyAllWindows()