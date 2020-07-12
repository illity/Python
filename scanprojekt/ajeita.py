raw = open('1to16.txt','r').read()
new = open('1to16f.txt','a')
lines = raw.split('\n')
count = 0
for line in lines:
# if '1' in line and 'Step' not in line and 'Soul' not in line:
 #if 'Step' in line: print(count); count=0
 if 'soul' in line:
  linespl=line.split(' soul')
  linex=linespl[0]
  new.write(linex[6:])
  count=count+1
  if count<299: new.write('\n')