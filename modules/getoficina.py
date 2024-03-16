import os
import re
import storage.oficina as of
from tabulate import tabulate

#Devuelve un listado con el codigo de Oficina y ciudad donde hay oficina
#3
def getAllcodigodeOficinayCiudad():
    codigoOficinayCiudad=[]
    for val in of.oficina:
        if val.get("ciudad")!= None:
            codigoOficinayCiudad.append({
                "Codigo de la oficina":val.get("codigo_oficina"),
                "Ciudad":val.get("ciudad")
            })
    return codigoOficinayCiudad
# Devuelve un listado con la ciudad y el telefono de las ciudades en España
def getAllCiudadytelefonoEspaña():
    ciudadyTelefonoSpain=[]
    for val in of.oficina:
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
                     
                            Reporte de Oficinas
              
              
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


        