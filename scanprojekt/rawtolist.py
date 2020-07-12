import re
a = open('raw.txt','r')
b = open('lista.txt', 'a')
raw=a.read()
lista=raw.split('\n')
for i in lista:
 if ' 1 ' in i:
  b.write(re.search(' 1 (.*) soul',i)[1]+'\n')
b.close()