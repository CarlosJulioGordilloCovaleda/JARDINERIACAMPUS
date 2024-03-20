from datetime import datetime
from tabulate import tabulate
import requests
import modules.getempleado as Ge

#Remote: http://172.16.104.20:5019 Servidos Pagos
def getAllDataPagos():
    peticion = requests.get("http://172.16.104.45:5019")
    data = peticion.json()
    return data
#http://172.16.104.45:5022  Clientes
def getAllDataClientes():
    peticion=requests.get("http://172.16.104.45:5022")
    data=peticion.json()
    return data




#Devuelve un listado con el codigo de cliente de aquello clientes
#que realizaron algun pago en 2008 tenga en cuenta que debera
#Eliminaraquellos codigos de cliente que aparezcan repetidos

def getCodigosClientes2008():
    CodigosClientes2008=set()
    for val in getAllDataPagos():
        fechaPago=(val.get("fecha_pago"))
        if fechaPago!=None:
            fechaPagoConvertida=datetime.strptime(fechaPago,"%Y-%m-%d")
            if fechaPagoConvertida.year==2008:
                CodigosClientes2008.add(val.get("codigo_cliente"))
    listaDeCodigos2008 = [{"Codigo Cliente": code} for code in CodigosClientes2008]
    return listaDeCodigos2008
#devuelve un listado de todos los pagos que se realizaron en el año 2008 
#mediante PayPal Ordene el resultado de mayor a menor

def getAllPagos2008Paypal():
    pagosRealizados=[]
    for val in getAllDataPagos():
        fechaPago=val.get("fecha_pago")
        if val.get("forma_pago")=="PayPal" and val.get("fecha_pago")!=None:
            fechaConverida=datetime.strptime(fechaPago,"%Y-%m-%d") 
            if fechaConverida.year==2008:
                pagosRealizados.append({
                    "codigo_cliente":val.get("codigo_cliente"),
                    "forma_pago":val.get("forma_pago"),
                    "id_transaccion":val.get("id_transaccion"),
                    "fecha_pago":val.get("fecha_pago"),
                    "total":val.get("total"),
                })
    pagosRealizados.sort(key=lambda x: x['total'], reverse=True)
    return pagosRealizados

def getAllNombreClientePagoRepVentas():
    ListaClientespagados=set()
    for val in getAllDataClientes():
        ListaClientespagados.add(
            val.get("codigo_cliente"),
        )
        ListaClientespagado=[{"Codigo del Cliente":code} for code in ListaClientespagados]
    lista2=[]
    for cliente in ListaClientespagado:
        for val2 in getAllDataClientes():
            if cliente.get("Codigo del Cliente")==val2.get("codigo_cliente"):
                lista2.append({
                    "Nombre del Cliente":val2.get("nombre_cliente"),
                    "Codigo del Vendedor":val2.get("codigo_empleado_rep_ventas")
                })
    listadef=[]
    for val3 in lista2:
        for val4 in Ge.gellAlldataEmpleados():
            if val3.get("Codigo del Vendedor")==val4.get("codigo_empleado"):
                listadef.append({
                    "Nombre del cliente":val3.get("Nombre del Cliente"),
                    "Nombre del representante de ventas":(f'{val4.get("nombre")} {val4.get("apellido1")}'),
                })
    return listadef
def getAllNombreClientequenohanpago():
    ListaClientespagados=set()
    for val in getAllDataClientes():
        ListaClientespagados.add(
            val.get("codigo_cliente"),
        )
        ListaClientespagado=[{"Codigo del Cliente":code} for code in ListaClientespagados]
    lista2=[]
    for cliente in ListaClientespagado:
        for val2 in getAllDataClientes():
            if cliente.get("Codigo del Cliente")!=val2.get("codigo_cliente"):
                lista2.append({
                    "Nombre del Cliente":val2.get("nombre_cliente"),
                    "Codigo del Vendedor":val2.get("codigo_empleado_rep_ventas")
                })
    listadef=[]
    for val3 in lista2:
        for val4 in Ge.gellAlldataEmpleados():
            if val3.get("Codigo del Vendedor")==val4.get("codigo_empleado"):
                listadef.append({
                    "Nombre del cliente":val3.get("Nombre del Cliente"),
                    "Nombre del representante de ventas":(f'{val4.get("nombre")} {val4.get("apellido1")}'),
                })
    return listadef
def menu():


    print(""" 
            
                      Reporte de Pagos
          
          1.listado con el codigo de cliente que realizaron algun pago en 2008 
          2.listado de todos los pagos que se realizaron en el año 2008  mediante PayPal de mayor a menor
          3.Ensayo

 """)
    
    opcion=int(input("Ingrese un numero : "))
    if opcion==1:
        print(tabulate(getCodigosClientes2008(),headers="keys",tablefmt="github"))
    elif opcion==2:
        print(tabulate(getAllPagos2008Paypal(),headers="keys",tablefmt="github"))
    elif opcion==3:
        print(tabulate(getAllNombreClientePagoRepVentas(),headers="keys",tablefmt="github"))
    elif opcion==4:
        print(tabulate(getAllNombreClientequenohanpago(),headers="keys",tablefmt="github"))

