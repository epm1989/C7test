from datetime import date,datetime,timedelta
import mysql.connector as mariadb

class Elconjunto():
    
    def __init__(self, *args, **kwargs):
        """
        (dominio,ip#1,ip#2)
        dominio es un string 
        ip una lista
        uno=Elconjunto(username='fgfg',secret='fgh#',theDatabase='gfggf')
        """
        if args:
            self._lalista=list(args)
            self.domain=self._lalista[0]
            self.ip=self._lalista[1::]
            
        else:
            print('no has agregado dominio e IP')
        
        if kwargs and (('username' in kwargs) and ('secret' in kwargs) and ('theDatabase' in kwargs)):
            self._username=kwargs['username']
            self.__secret=kwargs['secret']
            self._theDatabase=kwargs['theDatabase']
        else:
            print('kwars no son correctos check sintaxis')
            mensaje=''' 
            Ejemplo1
            Elconjunto(\'fgfg\',\'1.2.3.2\',\',5.25.6.5\',username=\'xxx\',ssecret=\'xxxxx\',theDatabase=\'xxxxxx\')

            Ejemplo2
            Elconjunto(username=\'xxx\',ssecret=\'xxxx\'#,theDatabase=\'xxxxxx\')
            '''
            print(mensaje)
        
    
    def connectDB(self):
        """
        uno.connectDB()
        """

        try:
            self._mariadb_connection = mariadb.connect(user=self._username, password=self.__secret, database=self._theDatabase)
            return True
        except:
            return False
    
    def disconnectDB(self):
        """
        uno.disconnectDB()
        """
        try:
            self._mariadb_connection.close()
            return True
        except:
            return False
    
    def insertTuple(self,eldomain, laip):
        """
        uno.insertTuple('hola.aff','4.2.5.4')
        """
        try:
            add_tuple = ("INSERT INTO dominios(name,active)VALUES ('{}',1)".format(eldomain))
            cursor=self._mariadb_connection.cursor()
            cursor.execute(add_tuple)
            self._mariadb_connection.commit()
            add_tuple = ("INSERT INTO ips(ip,dominio_id) VALUES ('{1}',(SELECT dominio_id FROM dominios WHERE name = '{0}' LIMIT 1))".format(eldomain,laip))
            cursor.execute(add_tuple)
            self._mariadb_connection.commit()
            cursor.close()
            return True
        except:
            return False
    
    def selectInfoTablesTuple(self):
        try:
            query = ("select dominios.dominio_id,name,ips.ip_id,ip from dominios inner join ips on ips.dominio_id = dominios.dominio_id where active = 1")
            cursor=self._mariadb_connection.cursor()
            cursor.execute(query)
            mydict=dict()
            for (dominio_id,name,ip_id,ip) in cursor:
                mydict[name]=[dominio_id,ip_id,ip]

            cursor.close()
        except:
            return False


        return mydict
    
    def insert_logs(self,dominio_id,ip_id,dominio,ipActual,ipNueva):
        """
        uno.insert_logs(1,11,'mydominio.local','9.9.8.8','7.7.5.5')
        """
        try:
            add_tuple = ("INSERT INTO logs(dominio_id,ip_id,description) VALUES ({0},{1},CONCAT('Se detecta un cambio en el dominio ','{2}',' con IP nueva ','{3} -> {4}'))".format(dominio_id,ip_id,dominio,ipActual,ipNueva))
            #print(add_tuple)
            cursor=self._mariadb_connection.cursor()
            cursor.execute(add_tuple)
            self._mariadb_connection.commit()
            cursor.close()
            return True
        except:
            return False
    
    def update_domain(self,dominio,active):
        """
        UPDATE dominios SET active = 0 WHERE dominio_id = (SELECT dominio_id FROM dominios WHERE name = 'fgfg'  LIMIT 1);
        uno.update_domain('hoaasla.aff')
        """
        try:
            
            add_tuple = ("UPDATE dominios SET active = {1} WHERE dominio_id = (SELECT dominio_id FROM dominios WHERE name = '{0}'  LIMIT 1)".format(dominio,active))
            #print(add_tuple)
            cursor=self._mariadb_connection.cursor()
            cursor.execute(add_tuple)
            self._mariadb_connection.commit()
            cursor.close()
            return True
        except:
            return False
        
"""
INICIALIZAR LA INSTANCIA
import os
#liux export C7flag='ccxxxxxxx' reinicar consola
thesecret=os.environ['C7flag']

#uno=Elconjunto('hola.cofdsm','1.24.3.2',username='esteban',secret=thesecret,theDatabase='CsieteTest')
uno=Elconjunto(username='esteban',secret=thesecret,theDatabase='CsieteTest')
uno.connectDB()

uno.insertTuple('wwww.asla.aff','4.2.88.4')

mio=uno.selectInfoTablesTuple()

uno.insert_logs(1,11,'mydominio.local','9.9.8.8','7.7.5.5')

#consulta sql
#select dominios.dominio_id,name,ips.ip_id,ip from dominios inner join ips on ips.dominio_id = dominios.dominio_id where active = 1;

uno.disconnectDB()

uno._theDatabase
uno._username
uno.__secret
uno.domain
uno.ip

actualizar campo
UPDATE dominios SET active = 0 WHERE dominio_id = (SELECT dominio_id FROM dominios WHERE name = 'fgfg'  LIMIT 1);
uno.update_domain('hoaasla.aff')

"""


