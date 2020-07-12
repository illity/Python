a = open('newlist.txt','r').read()
l=a.split('\n')
y=[]
cont = 0
print(l)
for null in l:
 if len(null)>1:
  if (int(null[len(null)-1])-1)>=1:
   y.append(null)
   cont=cont+1
print(*sorted(y),sep='\n')
print(cont)