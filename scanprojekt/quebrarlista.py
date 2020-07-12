l = open('newlist.txt','r').read()
names = []
qtds = []
lines = l.split('\n')
for line in lines:
 if len(line)>1:
  names.append(line.split(' - ')[0])
  qtds.append(line.split(' - ')[1])
namelist=''
qtdlist=''
for name in names:
 namelist = namelist+name+'\n'
for qtd in qtds:
 qtdlist = qtdlist+qtd+'\n'
x = open('names.txt','w')
x.write(namelist)
x.close()
x = open('qtd.txt','w')
x.write(qtdlist)
x.close()