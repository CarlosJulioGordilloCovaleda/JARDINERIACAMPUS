import storage.producto as po
#import storage.pago as pa
import storage.cliente as cli
from tabulate import tabulate

# Una lista que me de el nombre del producto y el codigo y la cantidad que aun hay, de todos los productos que tenga
# un stock igual o inferior a 15 unidades

def getAllNombreyCodigoproductostock50menoss():
    listarespuesta=[]
    for val in po.producto:
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
    for val in po.producto:
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
    for val in pa.pago:
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
            for cliente in cli.clientes:
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
#def getAllStocksPriceGama(gama,stock):
#    def defgamaStock(val):

def getAllStockPriceGamma(gama,stock):
    condiciones=[]
    for val in po.producto:
        if(val.get("gama") == gama and val.get("cantidad_en_stock")>stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")

def menu():
    print("""   
                        Reporte Productos
          
          1.Lista de los productos con un stock igual o menor a 15 unidades
          2.Lista de productos que mas utilidad generan
          3.TOP 5 MEJORES CLIENTES
 """)
    print()
    opcion=int(input("Digite el numero de la opcion seleccionada : "))
    print()
    if opcion==1:
        print(tabulate(getAllNombreyCodigoproductostock50menoss(),headers="keys",tablefmt="github"))
    
    elif opcion==2:
        print(tabulate(getAllNombreproductosygamamayorutilidad(),headers="keys",tablefmt="github"))

    elif opcion==3:
        print(tabulate(clientesquemascompran(),headers="keys",tablefmt="github"))

