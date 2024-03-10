from datetime import datetime
import storage.pago as pg
from tabulate import tabulate
#Devuelve un listado con el codigo de cliente de aquello clientes
#que realizaron algun pago en 2008 tenga en cuenta que debera
#Eliminaraquellos codigos de cliente que aparezcan repetidos

def getCodigosClientes2008():
    CodigosClientes2008=set()
    for val in pg.pago:
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
    for val in pg.pago:
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

def menu():

    print(""" 
            
                      Reporte de Pagos
          
          1.listado con el codigo de cliente que realizaron algun pago en 2008 
          2.listado de todos los pagos que se realizaron en el año 2008  mediante PayPal de mayor a menor

 """)
    
    opcion=int(input("Ingrese un numero : "))
    if opcion==1:
        print(tabulate(getCodigosClientes2008(),headers="keys",tablefmt="github"))
    elif opcion==2:
        print(tabulate(getAllPagos2008Paypal(),headers="keys",tablefmt="github"))
        

