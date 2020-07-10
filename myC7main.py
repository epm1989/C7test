from time import sleep;
from myC7class import Elconjunto
import os

global uno
thesecret=os.environ['C7flag']
uno=Elconjunto(username='esteban',secret=thesecret,theDatabase='CsieteTest')


def listar():
    
    uno.connectDB()
    mio=uno.selectInfoTablesTuple()
    uno.disconnectDB()
    if mio:
        print('DOMINIO','DIRECCION de RED')
        print('---------------------------')
        c=1
        for key,value in mio.items():
            print(c,key,value[2])
            c += 1
        print('___________________________')
    else:
        print('Fallo la lectura, intente de nuevo')
        sleep(1)

def borrar(eldominio,0):

    uno.connectDB()
    res=uno.update_domain(eldominio)
    if res:
        print('Movieminto Exitoso!!!')
    uno.disconnectDB()


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
        ##############################################
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
            if choice == 3:
                try:
                    entrada=input('Dijite el Dominio exactamente como fue listado: ')
                    entrada=entrada.replace('&','').replace('%','').replace(',','').replace(';','').replace(' ','')
                    borrar(entrada)
                except:
                    print('No se pudo procesar, caracteres invalidos!!!')
                    sleep(1)
                
        except ValueError as identifier:
            print(identifier)
            print('Debe de ingresar un Numero. no un texto')
        finally:
            sleep(2)



if __name__ == "__main__":
    run()