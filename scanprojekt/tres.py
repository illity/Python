a = open('oldlist.txt','r').read()
b = open('newlist.txt','r').read()
l=a.split('\n')
l2=b.split('\n')
y=[]
z=[]
cont = 0
for i in range(286):
 if len(l[i])>1:
  if (int(l[i][len(l[i])-1])-1)>=1:
   y.append(l[i].split(' - ')[0])
  if (int(l2[i][len(l2[i])-1])-1)>=1:
   z.append(l2[i].split(' - ')[0])
for null in z:
 if not null in y:
  print(null)
  cont=cont+1
print(cont)