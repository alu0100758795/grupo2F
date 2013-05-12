# uso de la funcio trapecio_senxpi

import sys, time
from math import *
from modulo_trapecio import trapecio_senxpi
from modulo_error import error

n=range(1,10)+range(10,110,10)

if __name__=='__main__':
  fichero=open('resultado.txt', 'w')
  
  e0 = time.time() # Unix epoch time
  c0 = time.clock() # CPU time
  
  fichero.write("Numero trapecio\nvalor metodo trapecio\nerror\nUnix epoch time\nCPU time\n")
  
  for i in range(len(n)):
    fichero.write("%i\n%2.10f\n" %(n[i],trapecio_senxpi(n[i])))
    fichero.write("%2.10f\n" %(error(trapecio_senxpi(n[i])))) 
    fichero.write("%s\n" %(time.time() - e0))
    fichero.write("%s\n" %(time.clock() - c0))
    i+=1
  fichero.close()