a = open('archie.txt','r').read()
b = open('quant.txt','r').read()
c = open('progress.txt','a')
la = a.split('\n')
lb = b.split('\n')
for i in range(len(la)):
 c.write(la[i]+' - '+lb[i])
 if i != len(la)-1: c.write('\n')