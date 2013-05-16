
import time
from math import *
from modulo_trapecio import trapecio_senxpi
from modulo_error import error

n=range(1,8,2)+range(8,20,4)+ range(100,300,100)

if __name__=='__main__':
  fichero=open('resultado.txt', 'w')
  
  e0 = time.time()
 
  for i in range(len(n)):
    fichero.write("%i\n%.10f\n%.10f\n" %(n[i], error(trapecio_senxpi(n[i])), time.time() - e0))
    i+=1
  fichero.close()
 
