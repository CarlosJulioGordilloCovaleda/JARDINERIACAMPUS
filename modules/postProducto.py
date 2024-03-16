import os
from tabulate import tabulate 
import json
import requests

def postProducto():
    producto={
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": input("Ingrese el nombre de la gama"),
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
        "precio_venta": int(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrse el precio del proveedor: "))    
    }
    
    peticion=requests.post ("http://192.168.1.16:5021",data=json.dumps(producto))
    res=peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")#Sirve para borrar el menu anteior seleccionado y no se haga un monton de informacion
        print("""
             
             ---------  Administrador de productos
             1. Guardar un producto nuevo
             0. Atras 
              """)
        opcion=int(input("Seleccione unas de las opciones : " ))
        if opcion==1:
            print(tabulate(postProducto(), headers="keys",tablefmt="github"))
            input("Presione una tecla para continuar ...")
        elif opcion==0:
            break
            