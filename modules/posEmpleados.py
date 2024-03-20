import re
import os
import requests
import modules.getempleado as Gem

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
                    name=input("Ingresa el nombre cel nuevo empleado : ")
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
                    apellido2=input("Ingresa el segundo apellido del nuevo empleado : ")
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
                            break
                        else:
                            raise Exception ("Ingrese la extension segun el estandar establecido")
                    else:
                        raise Exception("ERROR. Ingrese numeros")
            except Exception as error:
                print(error)                    
        print(empleadosDic)
       
        # "extension": "3897",
        # "email": "marcos@jardineria.es",
        # "codigo_oficina": "TAL-ES",
        # "codigo_jefe": null,
        # "puesto": "Director General"