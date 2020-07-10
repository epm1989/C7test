from time import sleep;
from myC7class import Elconjunto
import os
import dns.resolver

global uno,mio
thesecret=os.environ['C7flag']
uno=Elconjunto(username='esteban',secret=thesecret,theDatabase='CsieteTest')
mio=dict()

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

def borrar(eldominio,active):

    uno.connectDB()
    res=uno.update_domain(eldominio,active)
    if res:
        print('Movimeinto Exitoso!!!')
    uno.disconnectDB()

def agregar(eldominio):
    uno.connectDB()
    you=uno.selectDomains()

    existe=eldominio in you.keys()
    print(you.keys())
    print(you.values())
    print(existe)

    if existe:
        try:
            ipActual=you[eldominio][1]
            res=uno.update_domain(eldominio,1)
            resultDNS = dns.resolver.query(eldominio, 'A')
            ipNueva=resultDNS[0].to_text()
            print(ipActual,ipNueva)
            if not (ipActual == ipNueva ):
                print('sobreescribiendo IP...!!!!!!!')
                res=uno.updateTuple(eldominio, ipNueva)
                print(res)
                if res: print('update OK!!!!!!!')
                uno.insert_logs(you[eldominio][2],you[eldominio][3],eldominio,ipActual,ipNueva)
        except:
            print('ERROR: DNS request Networks')
    else:
        try:
            result = dns.resolver.query(eldominio, 'A')
            ipNueva=result[0].to_text()
            res=uno.insertTuple(eldominio, ipNueva)
        except:
            print('ERROR: DNS request Networks')
        

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
                    borrar(entrada,0)
                except:
                    print('No se pudo procesar, caracteres invalidos!!!')
                    sleep(1)
            if choice == 2:
                entrada=input('Dijite el Dominio adicionar: ')
                entrada=entrada.replace('&','').replace('%','').replace(',','').replace(';','').replace(' ','')
                agregar(entrada)    
        except ValueError as identifier:
            print(identifier)
            print('Debe de ingresar un Numero. no un texto')
        finally:
            sleep(2)



if __name__ == "__main__":
    run()