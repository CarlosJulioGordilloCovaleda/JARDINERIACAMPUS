import storage.empleado as em 
from tabulate import tabulate
#Devueelve el nombre  del puesto,nombre y apellido y emails del jefe de la empresa

def getAllPuestoNombreApellidosEmail(codigo_jefe):
    PuestoNombreApellidosEmail = []
    for val in em.empleados:
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
    for val in em.empleados:
            if(val.get("puesto")!="Representante Ventas"):
                NombreApellidosPuesto.append({
                "Nombre":val.get("nombre"),
                "apellidos":f"{val.get('apellido1')} {val.get('apellido2')}",
                "puesto":val.get("puesto")
                })
    return NombreApellidosPuesto

# Devuelve un listado con los nombres y apellidos y e-mails de los empleados cuyo Jefe tiene
#un codigo de jefe igual a 7

def getAllNombresApellidosEmailsempleadosJefe7():
    listadedatos=[]
    for val in em.empleados:
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