
from tabulate import tabulate
import requests

# "http://154.38.171.54:5003/empleados Puerto Servidor Profe
# http://192.168.1.16:5025 Puerto de empleado 
def gellAlldataEmpleados():
     peticion=requests.get("http://154.38.171.54:5003/empleados")
     data=peticion.json()
     return data
# Obtienes todos los codigos de los empleados
def getAllcodigos():
    codes=[]
    for val in gellAlldataEmpleados():
        codes.append(val.get("codigo_empleado"))
    return codes
# Obtiene todos los emails 
def getAllemails():
    emailslist=[]
    for val in gellAlldataEmpleados():
        emailslist.append(val.get("email"))         
    return emailslist
#Puestos de la empresa
def getAllpuestos():
    puestos=set()
    for val in gellAlldataEmpleados():
        puestos.add(val.get("puesto"))
    puestos_lista=list(puestos)
    return puestos_lista
# Directores de Oficina
def getAllpuestosdir():
    directoresoficina=list()
    for val in gellAlldataEmpleados():
        if val.get("puesto")=="Director Oficina":
            directoresoficina.append({
                "Puesto":val.get("puesto"),
                "Codigo Oficina":val.get("codigo_oficina"),
                "Codigo Empleado":val.get("codigo_empleado")
            })
    
    return directoresoficina

          
#Devueelve el nombre  del puesto,nombre y apellido y emails del jefe de la empresa
def getAllPuestoNombreApellidosEmail(codigo_jefe):
    PuestoNombreApellidosEmail = []
    for val in gellAlldataEmpleados():
        if (val.get("codigo_jefe")==None):
            PuestoNombreApellidosEmail.append({
                "puesto":val.get("puesto"),
                "nombre":val.get("nombre"),
                "apellidos":f"{val.get('apellido1')} {val.get('apellido2')}",
                "email":val.get("email")
           }) 
            return PuestoNombreApellidosEmail
#Devuele un listado con el nombre,apellido y puesto de aquellos empleados que no sean representantes de ventas
def getNombreApellidosPuesto():
    NombreApellidosPuesto= []
    for val in gellAlldataEmpleados():
            if(val.get("puesto")!="Representante Ventas"):
                NombreApellidosPuesto.append({
                "Nombre":val.get("nombre"),
                "apellidos":f"{val.get('apellido1')} {val.get('apellido2')}",
                "puesto":val.get("puesto")
                })
    return NombreApellidosPuesto
#Devuele un listado con el nombre,apellido y puesto de aquellos empleados que sean representantes de ventas
def getNombreApellidosPuestoRepVentas():
    NombreApellidosPuesto= []
    for val in gellAlldataEmpleados():
            if(val.get("puesto")=="Representante Ventas"):
                NombreApellidosPuesto.append({
                "Codigo":val.get("codigo_empleado"),
                "Nombre":val.get("nombre"),
                "apellidos":f"{val.get('apellido1')} {val.get('apellido2')}",
                "puesto":val.get("puesto")
                })
    return NombreApellidosPuesto
# Devuelve un listado con los nombres y apellidos y e-mails de los empleados cuyo Jefe tiene
#un codigo de jefe igual a 7

def getAllNombresApellidosEmailsempleadosJefe7():
    listadedatos=[]
    for val in gellAlldataEmpleados():
        if val.get("codigo_jefe")==7:
            listadedatos.append({
            "Nombres y Apellidos":(f'{val.get("nombre")} {val.get("apellido1")} {val.get("apellido2")}'),
            "E-mail " : val.get("email")
               })
    return listadedatos


def menu():
    print(""" 
                    
    ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗    ███████╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
    ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗      █████╗  ██╔████╔██║██████╔╝██║     █████╗  ███████║██║  ██║██║   ██║███████╗
    ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝      ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║  ██║██║   ██║╚════██║
    ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗    ███████╗██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██████╔╝╚██████╔╝███████║
    ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                                              

           
           1.   Datos del Jefe de la Empresa
           2.   Listado con el nombre,apellido y puesto de aquellos empleados que no sean representantes de ventas
           3.   Listado con el nombre,apellido y puesto de aquellos empleados que sean representantes de ventas
           4.   Listado con los nombres y apellidos y e-mails de los empleados cuyo Jefe tiene un codigo de jefe
                igual a 7

""")
    opcion=int(input(" Ingrese una opción : "))
    if opcion==1:
        codigo_jefe=None
        print(tabulate(getAllPuestoNombreApellidosEmail(codigo_jefe), headers="keys", tablefmt="github"))

    elif opcion==2:
         puesto="Representante Ventas"
         print(tabulate(getNombreApellidosPuesto(puesto),headers="keys", tablefmt="github"))
    
    elif opcion==3:
         puesto="Representante Ventas"
         print(tabulate(getNombreApellidosPuestoRepVentas(puesto),headers="keys", tablefmt="github"))
    
    
    elif opcion==4:
        print(tabulate(getAllNombresApellidosEmailsempleadosJefe7(),headers="keys",tablefmt="github"))