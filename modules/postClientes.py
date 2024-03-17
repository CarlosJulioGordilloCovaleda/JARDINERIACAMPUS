# Este modulo es para agregar nuevos clientes
import re
import requests
import os
import json
import modules.getclientes as clientes
from tabulate import tabulate

def postClientes():
    cliente=dict()
    while True:
        try:
            # Agregar Codigo CLiente
            if (not cliente.get("codigo_cliente")):
                Ultimocodigo=clientes.codigosClientes()[-1] # Se agrega automaticamente por que tiene una secuencia lineal
                cliente["codigo_cliente"]=Ultimocodigo+1
            #Agregar el nombre de la empresa
            if(not cliente.get("nombre_cliente")):
                clientenombre=input("Ingrese el nombre del cliente: ")
                cliente["nombre_cliente"]=clientenombre.title()
            #Agregar el nombre del contacto
            if(not cliente.get("nombre_contacto")):
                clientecontacto=input("Ingrese el nombre del contacto : ")
                if (re.match(r'^[a-zA-ZñÑ]+(?:\s+[a-zA-ZñÑ]+)*$',clientecontacto) is not None): #permite que se ingrese cero o más palabras adicionales después de la primera palabra, donde cada palabra está precedida por uno o más espacios (\s+). Y QUE SOLO CONTEGA LETRAS HASTA LA Ñ
                    cliente["nombre_contacto"]=clientecontacto.title()
                else:
                     raise Exception(" El nombre del contacto del cliente solo debe tener letras")
            # Agregar el primer Apellido
            if(not cliente.get("apellido_contacto")):
                clienteapellido=input("Ingrese el apellido del contacto : ")
                if (re.match(r'^[a-zA-ZñÑ]+(?:\s+[a-zA-ZñÑ]+)*$',clienteapellido) is not None): #permite que se ingrese cero o más palabras adicionales después de la primera palabra, donde cada palabra está precedida por uno o más espacios (\s+). Y QUE SOLO CONTEGA LETRAS HASTA LA Ñ
                    cliente["apellido_contacto"]=clienteapellido.title()
                    
                else:
                     raise Exception(" El apellido de contacto del cliente solo debe tener letras")
            # Telefono
            if(not cliente.get("telefono")):
                clientetelefono=input("Ingrese el telefono del contacto : ")
                if (re.match(r'^[\d\s()-]+$',clientetelefono) is not None):  # permite que se ingresen uno o más dígitos (\d), espacios (\s) y paréntesis (()) y guiones.
                    cliente["telefono"]=clientetelefono.title()
                else:
                     raise Exception(" El telefono de contacto del cliente solo puede tener numeros tambien es permitido usar'()' y '-' ")
            # Fax
            if(not cliente.get("fax")):
                clientefax=input("Ingrese el fax del contacto : ")
                if (re.match(r'^[\d\s()-]+$',clientefax) is not None):  # permite que se ingresen uno o más dígitos (\d), espacios (\s) y paréntesis (()) y guiones.
                    cliente["fax"]=clientefax.title()
                    
                else:
                     raise Exception(" El fac de contacto del cliente solo puede tener numeros tambien es permitido usar'()' y '-' ")
            # Dirección # 1
            if(not cliente.get("linea_direccion1")):
                clientedirección=input("Ingrese la dirección 1 del cliente : ")
                cliente["linea_direccion1"]=clientedirección.title()
            # Dirección # 2
            if(not cliente.get("linea_direccion2")):
                clientedirecciónopcional=input("Si el usuario tiene una 2da dirección ingresala sino solo pulsa enter: ")
                if clientedirecciónopcional.strip(): #  strip() se utiliza para eliminar cualquier espacio en blanco alrededor de la entrada del usuario
                    cliente["linea_direccion2"]=clientedirecciónopcional.title()
                else:
                    cliente["linea_direccion2"]= None
                break
        except Exception as error:
            print(error) 
    print(cliente)
    
    peticion=requests.post ("http://192.168.1.16:5022",data=json.dumps(cliente, indent=4).encode("UTF-8"))
    res=peticion.json()
    res["Mensaje"]="Cliente  Guardado"
    return[res]
    


    
    
    

    #     "codigo_cliente": 1,
    #     "nombre_cliente": "GoldFish Garden",
    #     "nombre_contacto": "Daniel G",
    #     "apellido_contacto": "GoldFish",
    #     "telefono": "5556901745",
    #     "fax": "5556901746",
    #     "linea_direccion1": "False Street 52 2 A",
    #     "linea_direccion2": null,
    #     "ciudad": "San Francisco",
    #     "region": null,
    #     "pais": "USA",
    #     "codigo_postal": "24006",
    #     "codigo_empleado_rep_ventas": 19,
    #     "limite_credito": 3000.0