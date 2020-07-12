import requests
import re
import random
for i in range(200):
 v=random.randint(0,64297000)
 print(v)
 r=requests.get('https://www.xvideos.com/video{}/'.format(v))
 if not 'deleted' in (re.findall('<title>(.*)</title>',r.text)[0]):
  print(re.findall('<title>(.*)</title>',r.text)[0])
  print('https://www.xvideos.com/video{}/'.format(v))