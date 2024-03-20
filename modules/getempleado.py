
from tabulate import tabulate
import requests

# http://192.168.1.16:5025 Puerto de empleado 
def gellAlldataEmpleados():
     peticion=requests.get("http://192.168.1.16:5025")
     data=peticion.json()
     return data
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
def getNombreApellidosPuesto(puesto):
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
                     Reporte Empleados
           
           1. Datos del Jefe de la Empresa
           2. Listado con el nombre,apellido y puesto de aquellos empleados que no sean representantes de ventas
           3. Listado con los nombres y apellidos y e-mails de los empleados cuyo Jefe tiene
              un codigo de jefe igual a 7

""")
    opcion=int(input(" Ingrese una opción : "))
    if opcion==1:
        codigo_jefe=None
        print(tabulate(getAllPuestoNombreApellidosEmail(codigo_jefe), headers="keys", tablefmt="github"))

    elif opcion==2:
         puesto="Representante Ventas"
         print(tabulate(getNombreApellidosPuesto(puesto),headers="keys", tablefmt="github"))
    
    elif opcion==3:
        print(tabulate(getAllNombresApellidosEmailsempleadosJefe7(),headers="keys",tablefmt="github"))