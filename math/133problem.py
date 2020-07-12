for i in range(1,100):
 for j in range(1,100):
  q=(str(i/j).replace('.',''))
  #q='1234'
  for k in range(len(q)-1):
   for l in range(k+1,len(q)):
     #print(q[:k+1])
     #print(q[k+1:l+1])
     if int(q[k+1:l+1])!=0:
      newq=str( int(q[:k+1])/int(q[k+1:l+1]) ).replace('.','')
      for m in range(len(newq)-1):
       if newq[:m+1]==str(i)+str(j):
        print(i)
        print(j)
        print('')