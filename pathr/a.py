import cv2
import numpy as np
import sys

#sys.setrecursionlimit(10000)

def vizinho(coord, ponto):
 x=[]
 for i in range(-1,2):
  for j in range(-1,2):
   if not ((i==0)*(j==0)):
    x.append(np.where(np.all(coord==[ponto[0]+i,ponto[1]+j],axis=1))[0])
 y=[]
 for el in x:
  if len(el):
   y.append(coord[el[0]])
 return y
   

def seguirorig(coord, traceback, ponto):
 if len(coord)==0:
  return []
 vizinhos=vizinho(coord,ponto)
 open('coordinates.md','a').write(str(ponto)+',')
 if len(vizinhos)==0:
  if len(np.where(np.all(coord==ponto,axis=1))[0]):
   coord=np.delete(coord,(np.where(np.all(coord==ponto,axis=1))[0][0]),axis=0)
  p=traceback[len(traceback)-1]
  traceback.pop(len(traceback)-1)
  seguir(coord,traceback,p)
 if len(vizinhos)>1:
  if len(np.where(np.all(coord==ponto,axis=1))[0]):
   coord=np.delete(coord,(np.where(np.all(coord==ponto,axis=1))[0][0]),axis=0)
  traceback.append(ponto)#aqui adiciona o ponto pra voltar caso encontre uma ilha
  seguir(coord,traceback,vizinhos[0])
 if len(vizinhos)==1:
  if len(np.where(np.all(coord==ponto,axis=1))[0]):
   coord=np.delete(coord,(np.where(np.all(coord==ponto,axis=1))[0][0]),axis=0)
  traceback.append(ponto)#aqui adiciona o ponto pra voltar caso encontre uma ilha
  return seguir(coord,traceback,vizinhos[0])
 for x in coord:
  coord=np.delete(coord,0,axis=0)

def seguir(coord, traceback, ponto):
 while len(coord)!=0:
  print(len(coord))
  vizinhos=vizinho(coord,ponto)
  if len(coord)>1:
   open('coordinates.md','a').write(str(ponto)+',')
  else:
   open('coordinates.md','a').write(str(ponto))
  if len(vizinhos)==0:
   if len(coord)==1: break
   if len(np.where(np.all(coord==ponto,axis=1))[0]):
    coord=np.delete(coord,(np.where(np.all(coord==ponto,axis=1))[0][0]),axis=0)
   p=traceback[len(traceback)-1]
   traceback.pop(len(traceback)-1)
   ponto=p
   continue
  if len(vizinhos)>1:
   if len(np.where(np.all(coord==ponto,axis=1))[0]):
    coord=np.delete(coord,(np.where(np.all(coord==ponto,axis=1))[0][0]),axis=0)
   traceback.append(ponto)#aqui adiciona o ponto pra voltar caso encontre uma ilha
   ponto=vizinhos[0]
   continue
  if len(vizinhos)==1:
   if len(np.where(np.all(coord==ponto,axis=1))[0]):
    coord=np.delete(coord,(np.where(np.all(coord==ponto,axis=1))[0][0]),axis=0)
   traceback.append(ponto)#aqui adiciona o ponto pra voltar caso encontre uma ilha
   ponto=vizinhos[0]
   continue




def path(img):
 coordenadas = np.where(img == 0)
 coordenadas = np.transpose(coordenadas)
 ponto = coordenadas[0]
 coordenadas = seguir(coordenadas,[],ponto)

def main():
 img = cv2.imread('gaara.png')
 img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
 img=cv2.threshold(img,254,255,cv2.THRESH_BINARY)[1]
 cv2.imshow('',img);cv2.waitKey(1)
 path(img)
if __name__=='__main__':
 main()