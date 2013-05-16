# El error obtenido usando el metodo del trapecio
import sys
from math import *

def error(valor_trapecio):
  valor_real=2/pi
  return abs(valor_real-valor_trapecio)

if __name__=='__main__':
  if len(sys.argv)==2:
    valor_trapecio=float(sys.argv[1])
    
    print error(valor_trapecio)
  else:
    print "El modo de uso es:%s <valor con metodo de trapecio>" % (sys.argv[0])
