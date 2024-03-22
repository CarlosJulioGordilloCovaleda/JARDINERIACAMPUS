import re
import os
import modules.getoficina as Gof
import pycountry
from countryinfo import CountryInfo
import modules.getclientes as clientes


def posoficina():
    oficinas=dict()
    while True:
        try:
            if "pais" not in oficinas:
                for i,val in enumerate(clientes.Countries(),start=1):
                    print(f'\t{i} {val}')
                opseleccionada=input("Ingrese el numero del Pais de la nueva oficina : ")
                if opseleccionada.isdigit():
                    if((re.match(r'^(?:1?\d?\d|2[0-4]\d|25[0-9])$',opseleccionada) is not None)): # Expresion regular me permite ingresar numeros del 1 al 249
                        opseleccionada=int(opseleccionada)
                        oficinas["pais"]=clientes.Countries()[opseleccionada-1]
                        
                    else:
                        raise Exception("Ingrese una de las opciones en pantalla")
                else:
                    raise Exception("El dato debe ser un numero")
            
            if "ciudad" not in oficinas:
                ciudad=input(" Ingrese la ciudad del cliente : ")
                if (re.match(r'^[a-zA-Z\s]+$',ciudad)) != None:
                    oficinas["ciudad"]=ciudad.title()
                else:
                    raise Exception("Ingrese solo letras")  
                #Oficina
            if "codigo _oficina" not in oficinas:
                ciudad=(oficinas["ciudad"][:3]).upper()
                pais=pycountry.countries.lookup(oficinas["pais"]).alpha_2
                code=ciudad+"-"+pais
                oficinas["codigo oficina"]=code
                # Region
            if "region" not in oficinas:
                pais=(oficinas["pais"])
                country_info=CountryInfo(pais)
                provincia=country_info.provinces()
                print("Lista de regiones")
                for i,val in enumerate(provincia,start=1):
                    print (f'\t{i} {val}')
                opcion=input("ingrese una opcion para seleccionar su región : ") 
                if opcion.isdigit():
                    opcion=int(opcion)
                    if opcion in range(1,len(provincia)+1):
                        oficinas["region"]=provincia[opcion-1]
                        break
                    else:
                        raise Exception("El numero ingresado no esta dentro del rango ")
                else:
                    raise Exception("Ingrese un numero entero ")  
        except Exception as error:
            print(error)
    print(oficinas)




        

        # "codigo_postal": "45632",
        # "telefono": "+34 925 867231",
        # "linea_direccion1": "Francisco Aguirre, 32",
        # "linea_direccion2": "5º piso (exterior)"

