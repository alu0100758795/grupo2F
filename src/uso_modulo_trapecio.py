
import sys, time
from math import *
from modulo_trapecio import trapecio_senxpi
from modulo_error import error

n=range(1,10)+range(10,110,10)

if __name__=='__main__':
  fichero=open('resultado.txt', 'w')
  
  e0 = time.time()
  
  fichero.write("n Valor Error Tiempo\n")
  
  for i in range(len(n)):
    fichero.write("%i %2.10f %2.10f %s\n" %(n[i],trapecio_senxpi(n[i]), error(trapecio_senxpi(n[i])), time.time() - e0))
    i+=1
  fichero.close()
