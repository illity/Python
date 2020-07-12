a = open('1to16f.txt','r').read()
b = open('1to16x.txt','r').read()
c = open('1to16c.txt','a')
l1=a.split('\n')
l2=b.split('\n')
print(len(l1)-len(l2))
for i in range(len(l1)):
 c.write(l1[i]+' - '+l2[i]+'\n')