#https://www.it-swarm.dev/es/python/como-ejecutar-una-funcion-de-forma-asincrona-cada-60-segundos-en-python/968384697/

#https://www.generacodice.it/es/articolo/348349/How-to-execute-a-function-asynchronously-every-60-seconds-in-Python

import threading
import time
global j
j=0

def miaa():
    h=23
    print(h)

def f():
    global j
    j += 1
    print("hello world {}".format(j))
    threading.Timer(3, f).start()

    #while(True):

    #    time.sleep(3)
    #    hola=input('Ingrese los datos:')

if __name__ == '__main__':
    f() 
    miaa()   
    time.sleep(20)
