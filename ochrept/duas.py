a = open('progress.txt','r').read()
b = open('archie.txt','r').read()
c = open('duas.txt','a')
l = a.split('\n')
count=0
for i in l:
 if len(i)>1:
  if int(i.split(' - ')[1])>=1:
   if i.split(' - ')[0] in b:
    print(i)
    c.write(i+'\n')
    count=count+1
print(count)