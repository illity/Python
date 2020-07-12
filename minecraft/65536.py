f=open('serpico.mcfunction','r').read()
c=f.split('\n')
i=0
#for el in c:
# i=i+1
# open('serpico{}.mcfunction'.format(int(i/65536)),'a').write(el+'\n')
for j in range(4):
 open('fullfunction.mcfunction','a').write('function custom:example/serpico{}\n'.format(j))