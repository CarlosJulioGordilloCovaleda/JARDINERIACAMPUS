#%USERPROFILE%\AppData\Local\Microsoft\WindowsApps;C:\Users\Carlos Gordillo\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\Carlos Gordillo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts;
import re
import os
from tabulate import tabulate
import requests

#Remote: http://192.168.1.16:5021 Productos
def allGetDataProductos():
    peticion=requests.get("http://172.16.106.242:5021/productos")
    data=peticion.json()
    return data
# Funcion que ayuda a eliminar los id
def getProductCodigoID(codigo):
    peticion=requests.get(f"http://172.16.106.242:5021/productos{codigo}")
    return [peticion.json()] if peticion.ok else []
  
# Funcion para llamar los Codigos de los productos y compararlos si ya esxisten
def getProductosCodigo(codigo):
    for val in allGetDataProductos():
        if (val.get("codigo_producto"))==codigo:
            return [val]
# Funcion para llamar a los nombres de los proveedores
def getNombresProveedores():
    proveedores=set()
    for val in allGetDataProductos():
        proveedores.add(val.get("proveedor"))
    proveedores_lista=list(proveedores)
    return proveedores_lista

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

# Remote: ttp://172.16.104.45:5024 Pedido
def allGetDataPedido():
    peticion=requests.get("http://172.16.104.45:5024")
    data=peticion.json()
    return data
# Remote http://172.16.104.45:5023 Detalle pedido

def allGetDataDetallepedido():
    peticion=requests.get("http://172.16.104.45:5023")
    data=peticion.json()
    return data


# Una lista que me de el nombre del producto y el codigo y la cantidad que aun hay, de todos los productos que tenga
# un stock igual o inferior a 15 unidades

def getAllNombreyCodigoproductostock50menoss():
    listarespuesta=[]
    for val in allGetDataProductos():
        if val.get("cantidad_en_stock")!=None:
            if val.get("cantidad_en_stock")<=15:
                listarespuesta.append({
                    "Codigo Producto":val.get("codigo_producto"),
                    "Nombre del Producto":val.get("nombre"),
                    "Cantidad en Bodega":(f'Hay {val.get("cantidad_en_stock")} unidades disponibles')
            })
    return listarespuesta
# Lista donde me de los productos que mas utilidad me dejan nombres de los productos y gama
def getAllNombreproductosygamamayorutilidad():
    listaresultados=[]
    mayor_utilidad=0
    for val in allGetDataProductos():
        if val.get("precio_venta")!=None and val.get("precio_proveedor")!=None:
            preciocompra=val.get("precio_proveedor")
            precioventa=val.get("precio_venta")
            utilidad=precioventa-preciocompra
            if utilidad>mayor_utilidad:
                mayor_utilidad=utilidad
                listaresultados.append({
                    "Nombre del Producto":val.get("nombre"),
                    "Gama del producto":val.get("gama"),
                    "Utilidad":(f'{utilidad} pesos')
                    })
            elif utilidad==mayor_utilidad:
                listaresultados.append({
                    "Nombre del Producto":val.get("nombre"),
                    "Gama del producto":val.get("gama"),
                    "Utilidad":(f'{utilidad} pesos')
                    })
                
    return listaresultados

# Un listado con los clientes que mas han comprado
def clientesquemascompran():
    totaldecomprasporcliente={}
    for val in getAllDataPagos():
        CodigoCliente=val.get("codigo_cliente")
        total=val.get("total")
        if CodigoCliente in totaldecomprasporcliente:
            totaldecomprasporcliente[CodigoCliente]=totaldecomprasporcliente[CodigoCliente]+total
        else:
            totaldecomprasporcliente[CodigoCliente]=total
        clientes_ordenados=sorted(totaldecomprasporcliente, key=totaldecomprasporcliente.get, reverse=True)
        clientesordenados3=clientes_ordenados[:5]
    listaresultado=[]
    for clientes in clientesordenados3:
            for cliente in getAllDataClientes():
                if clientes==cliente.get("codigo_cliente"):
                    listaresultado.append({
                        "Codigo":clientes,
                        "Nombre":cliente.get("nombre_cliente"),
                        "ventas (Dolares)":totaldecomprasporcliente[clientes]
                        
            })
     
    return listaresultado
#Devuelva una lista  con todos los productos que pertecen a la gama ornamentales y que tienen mas
# de 100 unidades en stock el listado debera estar organizado por su precio de venta,
# mostrando primer lugar los de mayor precio


def getAllStockPriceGamma(gama,stock):
    condiciones=[]
    for val in allGetDataProductos():
        if(val.get("gama") == gama and val.get("cantidad_en_stock")>stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")

def menu():
    while True:
        os.system("cls")
        print("""   
                        Reporte Productos
          
            1.Lista de los productos con un stock igual o menor a 15 unidades
            2.Lista de productos que mas utilidad generan
            3.TOP 5 MEJORES CLIENTES
            0.Volver
            
 """)
    
        op = input("Seleccione una de las siguientes opciones ")
        if (re.match(r'[0-9]+$',op) is not None):
            op=int(op)
            if(op >=0 and op<=7):
                if op==1:
                    print(tabulate(getAllNombreyCodigoproductostock50menoss(),headers="keys",tablefmt="github"))
                
                elif op==2:
                    print(tabulate(getAllNombreproductosygamamayorutilidad(),headers="keys",tablefmt="github"))

                elif op==3:
                    print(tabulate(clientesquemascompran(),headers="keys",tablefmt="github"))
                elif op==0:
                    break

