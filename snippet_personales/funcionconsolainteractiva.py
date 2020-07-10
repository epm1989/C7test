from time import sleep;


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
    except ValueError as identifier:
        print(identifier)
        print('Debe de ingresar un Numero. no un texto')
    finally:
        sleep(2)