import re
import os
import requests
import modules.getempleado as Gem
import modules.getoficina as Gof
from tabulate import tabulate

def postEmpleados():
        empleadosDic=dict()
        while True:
            try:
            # Codigo Empleado      
                if(not empleadosDic.get("codigo_empleado")):
                    codigoempleado=(Gem.getAllcodigos()[-1])+1
                    empleadosDic["codigo_empleado"]=codigoempleado

            #nombre"
                if "nombre" not in empleadosDic:
                    name=input("Ingresa el nombre del nuevo empleado : ")
                    if(re.match(r'^[a-zA-Z\s]+$',name) !=None): #Esta expresion regular sirve para colocar el nombre permite solo letras y espacios
                        empleadosDic["nombre"]=name.title()
                        
                    else:
                        raise Exception("Error Ingrese el nombre con solo letras")
            #Apellido 1"
                if "apellido1" not in empleadosDic:
                    apellido1=input("Ingresa el  primer apellido del nuevo empleado : ")
                    if(re.match(r'^[a-zA-Z]+$',apellido1)) != None:
                        empleadosDic["apellido1"]=apellido1.title()
                        
                    else:
                        raise Exception("Error Ingrese el Apellido con solo letras")
            #Apellido 2"
                if "apellido2" not in empleadosDic:
                    apellido2=input("Ingresa el segundo apellido del nuevo empleado: ")
                    if(re.match(r'^[a-zA-Z]+$',apellido2) !=None):
                        empleadosDic["apellido2"]=apellido2.title() 
                    else:
                        raise Exception("Error Ingrese el Apellido con solo letras")
            #Extensión
                if "extension" not in empleadosDic:
                    op=input("Ingrese la extension recuerde que son solo 4 numeros: ")
                    if op.isdigit():
                        if(re.match(r'^\d{4}$',op)!= None):
                            empleadosDic["extension"]=op
                        else:
                            raise Exception ("Ingrese la extension segun el estandar establecido")
                    else:
                        raise Exception("ERROR. Ingrese numeros")
            #Email
                if "email" not in empleadosDic:
                    letra_1=empleadosDic["nombre"][0].lower()
                    dominio="@jardineria.es"
                    emailasignado=letra_1+(empleadosDic["apellido1"].lower())+dominio # Concatenación
                    if emailasignado in Gem.getAllemails():
                        emailasignado=emailasignado+(empleadosDic["apellido2"])
                        empleadosDic["email"]=emailasignado
                    else:
                        empleadosDic["email"]=emailasignado
                    
            #"codigo_oficina"
                if "codigo_oficina" not in empleadosDic:
                    print("Oficinas de la Jarineria Campus")
                    for indice,val in enumerate(Gof.getAllcodigodeOficina(),start=1):
                        print(f'\t{indice} {val}')   
                    opcion=input("Seleccione un numero para un codigo de Oficina = ")
                    if opcion.isdigit():
                        opcion=int(opcion)
                        if opcion in range (1,len(Gof.getAllcodigodeOficina())+1):
                            empleadosDic["codigo_oficina"]=Gof.getAllcodigodeOficina()[opcion-1]
                        else:  
                            raise Exception(" Ingrese una de las opciones validas")    
                    else:
                        raise Exception (" Ingrese un numero")
                if "codigo_jefe" not in empleadosDic :
                    ubicaciones = {
                                    "MAD-ES": 7,
                                    "BCN-ES": 11,
                                    "PAR-FR": 15,
                                    "SFC-USA": 18,
                                    "BOS-USA": 20,
                                    "TOK-JP": 23,
                                    "LON-UK": 26,
                                    "TAL-ESP":3
                                }
                    if empleadosDic["codigo_oficina"] in ubicaciones:
                        empleadosDic["codigo_jefe"]=ubicaciones[empleadosDic["codigo_oficina"]]
                        
                    else:
                        print("Se reporta directamente con el Director General")
                        empleadosDic["codigo_jefe"]=1
                    
                if "puesto" not in empleadosDic:
                    xpuesto=input("Ingrese el puesto del nuevo empleado: ")
                    if (re.match(r'^[a-zA-Z\s]+$',xpuesto)!=None):
                        empleadosDic["puesto"]=xpuesto.title()
                        break
                    else:
                        raise Exception ("Ingrese solo letras para el puesto del nuevo empleado ")         
            except Exception as error:
                print(error)                    
        print(empleadosDic)
       

       
        # "puesto": "Director General"