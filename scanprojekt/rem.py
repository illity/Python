l = open('newlist.txt','r').read()
nl = open('novalista.txt','w')
list=l.split('\n')
newlist=''
for i in range(286):
 newlist=newlist+(list[i][:len(list[i])-1]+str(int(list[i][len(list[i])-1])-1))+'\n'
nl.write(newlist)
nl.close()