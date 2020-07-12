def add(name):
 a = open('1to16c.txt','r').read()
 l=a.split('\n')
 for i in range(len(l)):
  if name in l[i]:
   print(l[i])
   if(input('confirm?')=='y'):
    l[i]=l[i][:len(l[i])-1]+str(int(l[i][len(l[i])-1])+1)
    lista=''
    for x in l:
     if x!='':
      lista=lista+x+'\n'
    b = open('1to16c.txt','w')
    b.write(lista)
    b.close()
    print('added')
    break
   else:
    print('nothing done')

def rem(name):
 a = open('1to16c.txt','r').read()
 l=a.split('\n')
 for i in range(len(l)):
  if name in l[i]:
   print(l[i])
   if(input('confirm?')=='y'):
    l[i]=l[i][:len(l[i])-1]+str(int(l[i][len(l[i])-1])-1)
    lista=''
    for x in l:
     if x!='':
      lista=lista+x+'\n'
    b = open('1to16c.txt','w')
    b.write(lista)
    b.close()
    print('removed')
    break
   else:
    print('nothing done')

while(1):
 add(input())