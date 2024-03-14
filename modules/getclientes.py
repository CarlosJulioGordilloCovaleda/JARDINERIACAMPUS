
from tabulate import tabulate
import storage.empleado as em
import requests

#http://172.16.104.45:5022 Direcciòn Clientes
def getAllDataClientes():
    peticion=requests.get("http://172.16.104.45:5022")
    data=peticion.json()
    return data
# Devuelve un listado con todos los nombres de los clientes españoles


def Nombres():
    Nombres = []
    for val in getAllDataClientes():
        if (val.get("pais") == "Spain"):
            Nombres.append({
                "Nombre del cliente": val.get("nombre_cliente")
            })
    return Nombres

# Devuelve un listado con todos los clientes que sean de la ciudad de madrid y cuyo representante de venta tenga 
#El codigo de empleado11 0 30

def getAllCliMadridRepreVen():
    listaresultado=[]
    
    for val in getAllDataClientes():
        if val.get("ciudad")=="Madrid":
            if val.get("codigo_empleado_rep_ventas")==11 or val.get("codigo_empleado_rep_ventas")==30:  
                listaresultado.append({
                    "Codigo del cliente":val.get("codigo_cliente"),
                    "Nombre del cliente":val.get("nombre_cliente"),
                    "Ciudad":val.get("ciudad"),
                    "Codigo emp. Rep Ventas":val.get("codigo_empleado_rep_ventas")
                })
    return listaresultado

# Obten un listado con el nombre de cada cliente y el nombre y el apellido de su representante de ventas.
def getAllNombreClientesyNombreyApellidoEmpleados():
    resultado=[]
    for val in getAllDataClientes():
        resultado.append({
            "Nombre_Cliente":val.get("nombre_cliente"),
            "Codigo_Cliente":val.get("codigo_empleado_rep_ventas")
        })
        listaresultado=[]
    for cliente in resultado:
        for val2 in em.empleados:
            if cliente.get("Codigo_Cliente")==val2.get("codigo_empleado"):
                listaresultado.append({
                    "Nombre Cliente":cliente.get("Nombre_Cliente"),
                    "Datos del Representante Venta":(f'{val2.get("nombre")} {val2.get("apellido1")}'),
                    "Codigo de Empleado":cliente.get("Codigo_Cliente")

                })
    return listaresultado
# Muestra el nombre de los clientes que hayan realizado pagos juntos con el nombre de su representante de ventas


def menu():
    while True:
        print(""" 

                Reporte de los clientes
            0. Atras
            1. Obtener los nombres de los clientes Españoles
            2.listado con todos los clientes que sean de la ciudad de madrid
              y cuyo representante de venta tenga el codigo de empleado 11 0 30
            3. Ensayo
            

    """)
        print()
        opcion = int(input("Seleccione una opcion : "))
        if opcion == 1:
            print()
            print(tabulate(Nombres(), headers="keys", tablefmt="github"))
        elif opcion == 2:
            print()
            print(tabulate(getAllCliMadridRepreVen(), headers="keys", tablefmt="github"))
        elif opcion ==3:
            print(tabulate(getAllNombreClientesyNombreyApellidoEmpleados(),headers="keys", tablefmt="github"))
        elif opcion==0:
            break



