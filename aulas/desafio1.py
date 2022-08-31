import time
import numpy as np
 

def div(numero):
    for i in range(1,numero+1):
        if numero % i == 0:
            print(i)
            
def divisor(numero):
    n = np.arange(1,numero+1) # o 1 é o start do range
                            
    d = numero % n          # calculando o resto
    resto = d == 0          
    print(n[resto], numero) # vai printar os indices onde for verdadeiro

# inicio = time.time()  
# divisor(100888886)
# fim = time.time()

inicio = time.time()  
div(100888886)
fim = time.time()
print('Tempo:', (fim-inicio)/1000)

