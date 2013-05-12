# funcion metodo de trapecio de senx*pi desde -2 a -1

import sys
from math import *

def trapecio_senxpi(n):
  a=-2
  b=-1
  h=(b-a)/float(n)
  s=(sin(a*pi)+sin(b*pi))/float(2)
  for i in range(1,n):
    s+=sin(pi*(a+i*h))
  return h*s

if __name__=='__main__':
  if len(sys.argv)==2:
      n=int(sys.argv[1])	# n es el numero de trapecio deseado
      
      print trapecio_senxpi(n)    
  else:
    print "el modo de uso es:%s numero de trapecio" % (sys.argv[0])
     
    