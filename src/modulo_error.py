# modulo error

import sys
from math import *

def error(valor_trapecio):
  valor_real=2/float(pi)
  return abs(valor_real-valor_trapecio)

if __name__=='__main__':
  if len(sys.argv)==5:
    valor_trapecio=float(sys.argv[1])
    
    print error(valor_trapecio)
  else:
    print "el modo de uso es:%s valor con metodo de trapecio" % (sys.argv[0])
