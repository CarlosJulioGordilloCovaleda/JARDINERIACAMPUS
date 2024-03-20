import requests
import os 
import re
import json
import modules.getclientes as clientes
from tabulate import tabulate
import modules.getpagos as pag

def Pospagos():
    pago=dict()
    while True:
        try:
            # Agregar codigo cliente
            if (not pago.get("codigo_cliente")):
                data=clientes.codigosClientes()
                datostabla=clientes.codigosClientesyNombre()
                print(tabulate(datostabla, headers="keys", tablefmt="github"))
                print()
                codigocliente=input("Ingrese el codigo del cliente que realizo el pago: ")
                if codigocliente.isdigit():
                    codigocliente=int(codigocliente)
                    if codigocliente in data:
                        pago["codigo_cliente"]=codigocliente
                    else:
                        raise Exception (" El codigo ingresado no ha sido asignado a ningun cliente")
                else:
                    raise Exception("Condigo incorrecto ingrese nuevamente el codigo") 
            # Forma de Pago         
            if(not pago.get("forma_pago")):
                for i,val in enumerate(pag.formadepago(),start=1):
                    print(f'\t{i} {val}')
                opcion=input("Ingrese la forma de pago seleccionada: ")
                if opcion.isdigit():
                    opcion=int(opcion)
                    if opcion in range (1,len(pag.formadepago())+1):
                        pago["forma_pago"]=pag.formadepago()[opcion-1]
                        
                    else:
                        raise Exception ("Ingrese un metodo de pago de las opciones")
                else:
                    raise Exception("Ingrese un numero")
            # Fecha de Pago
            if(not pago.get("fecha_pago")):
                fechapago=input("Ingresa la fecha de pago en el siguiente formato YYYY-MM-DD Todo en numeros: ") 
                if((re.match(r'^\d{4}-(0[1-9]|1[0-2])-([0-2][0-9]|3[01])$',fechapago)) is not None): # Expresion regular es para fechas en años mes y dia que los meses sean entre 1 y 12 y los dias de 1 a 31
                    pago["fecha_pago"]=fechapago
                
                else:
                    raise Exception("Formato Incorrecto,ingrese nuevamente la fecha de pago")
            # total 
            if(not pago.get("total")):
                pagototal=input("Ingrese el pago del cliente: ")
                if pagototal.isdigit():
                    pagototal=int(pagototal)        
                    if pagototal!=None:
                        pago["total"]=pagototal
                        break
                    else:
                        raise Exception("Agregue el valor cancelado")
                else:
                    raise Exception("Ingrese el pago sin decimales")
        except Exception as error:
            print(error)
    print(pago)

            # "codigo_cliente": 1,
            # "forma_pago": "PayPal",
            # "id_transaccion": "ak-std-000001",
            # "fecha_pago": "2008-11-10",
            # "total": 2000
