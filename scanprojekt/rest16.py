a = open('1to16c.txt').read()
l = a.split('\n')
count=0
for i in l:
 if '0' in i:
  print(i)
  count=count+1
print(count)