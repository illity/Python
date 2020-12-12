from math import *
def xc(C,f):
 return 1/(C*2*pi*f)
def xl(L,f):
 return L*2*pi*f
def L(xL,f):
 return xL/(2*pi*f)
def C(xC,f):
 return 1/(xC*2*pi*f)
def Z(*args):
 condutancia=0
 for el in args:
  condutancia+=1/el
 return 1/condutancia