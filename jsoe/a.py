v=1
uva=5
def iscube(num):
 return (round(num**(1/uva))**uva==num)
for uva in range(3,20):
 print(uva)
 for i in range(1,5000):
  for j in range(i+1,5000):
   if (iscube(i**uva+j**uva)):
    print(i)
    print(j)
    print(uva)