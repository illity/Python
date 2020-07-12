import sys
print(sys.argv[1])
l = open('newlist.txt','r').read()
li = l.split('\n')
for i in li:
 if sys.argv[1] in i:
  print(i)