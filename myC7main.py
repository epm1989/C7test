from time import sleep;
from myC7class import Elconjunto
import os


def listar():
    thesecret=os.environ['C7flag']
    uno=Elconjunto(username='esteban',secret=thesecret,theDatabase='CsieteTest')
    uno.connectDB()
    mio=uno.selectInfoTablesTuple()
    uno.disconnectDB()
    if mio:
        print(mio.keys())
    else:
        print('Fallo la lectura, intente de nuevo')
        sleep(1)

def run():
    while True:
        saludo='''
        ##############################################
        ######Bienvenido a la prueba de Csiete.#######
        ##############################################
        '''
        print(saludo)
        
        opciones='''
        -->>>>>>>
        1. Listar Dominios.
        2. Agregar Dominios.
        3. Borrar Dominio.
        4. Abortar.
        -->>>>>>>
        :'''
        try:
            choice=input(opciones)
            choice=int(choice)
            if choice > 4 or choice == 0:
                raise ValueError('Opcion fuera del rango.')
            if choice == 4 :
                break

            if choice == 1:
                listar()
        except ValueError as identifier:
            print(identifier)
            print('Debe de ingresar un Numero. no un texto')
        finally:
            sleep(2)



if __name__ == "__main__":
    run()