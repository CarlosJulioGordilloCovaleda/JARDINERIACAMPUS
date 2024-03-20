# Este modulo es para agregar nuevos clientes
import re
import requests
import os
import json
import modules.getclientes as clientes
from tabulate import tabulate
import pycountry
from countryinfo import CountryInfo
import modules.getempleado as Ge

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
            # Pais
            if(not cliente.get("pais")):
                print("Lista de Paises")
                for i,val in enumerate(clientes.Countries(),start=1):
                    print (f'\t{i} {val}')
                opseleccionada=input("Ingrese el numero del Pais del cliente : ")
                if((re.match(r'^(?:1?\d?\d|2[0-4]\d|25[0-9])$',opseleccionada) is not None)): # Expresion regular me permite ingresar numeros del 1 al 249
                    opseleccionada=int(opseleccionada)
                    cliente["pais"]=clientes.Countries()[opseleccionada-1]
                    if cliente["pais"]=="United States":
                            cliente["pais"]="USA"
                    else:
                        cliente["pais"]=clientes.Countries()[opseleccionada-1]
                else:
                    raise Exception ("Elije una de las opciones presentadas: ")
            # Region    
            if(not cliente.get("region")):
                pais=(cliente["pais"])
                country_info=CountryInfo(pais)
                provincia=country_info.provinces()
                print("Lista de regiones")
                for i,val in enumerate(provincia,start=1):
                    print (f'\t{i} {val}')
                opcion=input("ingrese una opcion para seleccionar su región : ") 
                if opcion.isdigit():
                    opcion=int(opcion)
                    if opcion in range(1,len(provincia)+1):
                        cliente["region"]=provincia[opcion-1]
                    else:
                        raise Exception("El numero ingresado no esta dentro del rango ")
                else:
                    raise Exception("Ingrese un numero entero ")      
            #codigo_empleado_rep_ventas
            if (not cliente.get("codigo_empleado_rep_ventas")):
                print("Lista de representates en ventas con su codigo")
                data=Ge.getNombreApellidosPuestoRepVentas()
                print(tabulate(data,headers="keys",tablefmt="github"))
                opcion=(input("Escriba el codigo del representate de ventas que desea asignar al cliente : "))
                if opcion.isdigit():
                    opcion=int(opcion)
                    codes=[]
                    for val in data:
                        codes.append(val.get("Codigo"))
                    if opcion in codes:
                        cliente["codigo_empleado_rep_ventas"]=opcion
                    else:
                        raise Exception("Agregue una opcion valida")
                else:
                    raise Exception("Ingrese solo el codigo numerico")
            #Ingrese la ciudad
            if(not cliente.get("ciudad")):
                clienteciudad=input(" Ingrese la ciudad del cliente : ")
                cliente["ciudad"]=clienteciudad.title()
            #Ingrese el codigo Postal
            if(not cliente.get("codigo_postal")):
                clientecodigopostal=input("Ingrese el codigo postal del cliente : ")
                if clientecodigopostal.isdigit():
                    if (re.match(r'^\d{4,8}$',clientecodigopostal)is not None):
                        cliente["codigo_postal"]=clientecodigopostal
                    else:
                        raise Exception("Ingresa el codigo postal bajo las condicones estandar")
                else:
                    raise Exception("Ingrese un numero")
            #Ingrese limite_Credito
            if(not cliente.get("limite_credito")):
                clientecredito=input("Ingrese el limite de credito del cliente: ")
                if clientecredito.isdigit():
                    clientecredito=float(clientecredito)        
                    if clientecredito!=None:
                        cliente["limite_credito"]=clientecredito
                        break
                    else:
                        raise Exception("Si no se otorga cupo al cliente ingrese 0")
                else:
                    raise Exception("Ingrese un numero")
            
                
        except Exception as error:
            print(error) 
    print(cliente)
    
    # peticion=requests.post ("http://192.168.1.16:5022",data=json.dumps(cliente, indent=4).encode("UTF-8"))
    # res=peticion.json()
    # res["Mensaje"]="Cliente  Guardado"
    # return[res]
    
    #     "ciudad": "San Francisco",
    #     "codigo_postal": "24006",
    #     "limite_credito": 3000.0