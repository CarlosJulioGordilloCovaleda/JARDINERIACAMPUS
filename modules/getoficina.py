import os
import re
from tabulate import tabulate
import requests
# "http://154.38.171.54:5005/oficinas" Servidor Profe
# Puerto Oficina http://172.16.106.118:5026
def getAllDataoficina():
    peticion = requests.get("http://154.38.171.54:5005/oficinas")
    data = peticion.json()
    return data
#Devuelve un listado con el codigo de Oficina y ciudad donde hay oficina
def getAllcodigodeOficinayCiudad():
    codigoOficinayCiudad=[]
    for val in getAllDataoficina():
        if val.get("ciudad")!= None:
            codigoOficinayCiudad.append({
                "Codigo de la oficina":val.get("codigo_oficina"),
                "Ciudad":val.get("ciudad")
            })
    return codigoOficinayCiudad

# Devuelve un listado con los codigos de las oficinas
def getAllcodigodeOficina():
    codigoOficina=[]
    for val in getAllDataoficina():
        codigoOficina.append(val.get("codigo_oficina"))
    return codigoOficina


# Devuelve un listado con la ciudad y el telefono de las ciudades en España
def getAllCiudadytelefonoEspaña():
    ciudadyTelefonoSpain=[]
    for val in getAllDataoficina():
        if val.get("pais")=="España":
            ciudadyTelefonoSpain.append({
                "Ciudad":val.get("ciudad"),
                "N° Telefeono":val.get("telefono")
            })
    return ciudadyTelefonoSpain

def menu():
    while True:
        os.systema("cls")
        print(""" 
                     
                            
██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗    ██████╗ ███████╗     ██████╗ ███████╗██╗ ██████╗██╗███╗   ██╗ █████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔════╝    ██╔═══██╗██╔════╝██║██╔════╝██║████╗  ██║██╔══██╗██╔════╝
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗      ██║  ██║█████╗      ██║   ██║█████╗  ██║██║     ██║██╔██╗ ██║███████║███████╗
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝      ██║  ██║██╔══╝      ██║   ██║██╔══╝  ██║██║     ██║██║╚██╗██║██╔══██║╚════██║
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗    ██████╔╝███████╗    ╚██████╔╝██║     ██║╚██████╗██║██║ ╚████║██║  ██║███████║
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                                                                                                                           
      
          1. Listado de codigo de oficina y en que ciudad se ubica
          2. Listado de las oficinas ubicadas en España con su numero de telefono y correspondiente ciudad
 """)
           
        op = input("Seleccione una de las siguientes opciones ")
        if (re.match(r'[0-9]+$',op) is not None):
               op=int(op)
               if(op >=0 and op<=7):
                    if op==1:
                        print(tabulate(getAllcodigodeOficinayCiudad(), headers="keys",tablefmt="github"))
                    elif op==2:
                        print(tabulate(getAllCiudadytelefonoEspaña(), headers="keys", tablefmt="github"))


        