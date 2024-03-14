
from datetime import datetime
from tabulate import tabulate
import requests

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

#Devuelve un listado con los distintos estados por los que puede pasar un pedido
def getAllDiferentesEstados():
    DiferentesEstados=set()
    for val in allGetDataDetallepedido():
        if val.get("estado") != None:
            DiferentesEstados.add(val.get("estado"))
    lista_DiferentesEstados=[{"Estado del pedido": vall} for vall in DiferentesEstados]
    return lista_DiferentesEstados
# Devuelve un listado con el codigo de pedido,
#codigo de cliente,fecha esperada y fecha de entrega 
#de los pedidos que no han sido entregados a tiempos

def getAllPedidosEntregadosAtrasadosdeTiempo():
    pedidosEntregado=[]
    for val in allGetDataDetallepedido():
        if val.get("estado")== "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"]=val.get("fecha_esperada")
        if val.get("estado")=="Entregado":
            date_1=(val.get("fecha_entrega"))
            date_2=(val.get("fecha_esperada"))
            star= datetime.strptime(date_1,"%Y-%m-%d")
            end= datetime.strptime(date_2,"%Y-%m-%d")
            diff=end.date()-star.date()
            if diff.days<0:
                pedidosEntregado.append({
                    "Codigo del Pedido":val.get("codigo_pedido"),
                    "Codigo del Cliente":val.get("codigo_cliente"),
                    "Fecha Esperada":val.get("fecha_esperada"),
                    "Fecha de Entrega":val.get("fecha_entrega")
                })
    return pedidosEntregado

# Devuelve un listado con el codigo de pedido, codigo de cliente fecha esperada y fecha de entrega
#de los pedidos cuya fecha de entrega ha sidoal menos dos dias de la fecha esperada

def getAllPedidosEntregadosdosdiasantesdeTiempo():
    pedidosEntregado=[]
    for val in allGetDataDetallepedido():
        if val.get("estado")== "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"]=val.get("fecha_esperada")
        if val.get("estado")=="Entregado":
            date_1=(val.get("fecha_entrega"))
            date_2=(val.get("fecha_esperada"))
            star= datetime.strptime(date_1,"%Y-%m-%d")
            end= datetime.strptime(date_2,"%Y-%m-%d")
            diff=end.date()-star.date()
            if diff.days>=2:
                pedidosEntregado.append({
                    "Codigo del pedido":val.get("codigo_pedido"),
                    "Codigo del Cliente":val.get("codigo_cliente"),
                    "Fecha esperada":val.get("fecha_esperada"),
                    "Fecha de Entrega":val.get("fecha_entrega")
                })
    return pedidosEntregado

#Devuelve un listado dde todos los pedidos que fueron rechazados en  2009

def getAllPedidosRechazados2009():
    pedidosEntregado=[]
    for val in allGetDataDetallepedido():
        fechapedido=val.get("fecha_pedido")
        if val.get("estado")== "Rechazado" and val.get("fecha_pedido")!=None:
            fechaconvertida=datetime.strptime(fechapedido,"%Y-%m-%d")
            if fechaconvertida.year==2009:
                pedidosEntregado.append({
                    "Cod. pedido":val.get("codigo_pedido"),
                    "Fec. pedido":val.get("fecha_pedido"),
                    "Fec. esperada":val.get("fecha_esperada"),
                    "Fec. entrega":val.get("fecha_entrega"),
                    "Estado":val.get("estado"),
                    #"Comentarios":val.get("comentario"),
                    "Cod. cliente":val.get("codigo_cliente")
                })
    return pedidosEntregado

#Deuelve un listado de todos los pedidos que han sido entregados en el mes de enero de cualquier año

def getAllPedidosEntregadosdelmesdeenero():
    pedidosEntregado=[]
    for val in allGetDataDetallepedido():
        fechaEntrega=val.get("fecha_entrega")
        if val.get("estado")=="Entregado" and val.get("fecha_entrega")!=None:
            fechaconvertida=datetime.strptime(fechaEntrega,"%Y-%m-%d")
            if fechaconvertida.month==1:
                pedidosEntregado.append({
                    "Codigo pedido":val.get("codigo_pedido"),
                    "Fecha pedido":val.get("fecha_pedido"),
                    "Fecha esperada":val.get("fecha_esperada"),
                    "Fecha entrega":val.get("fecha_entrega"),
                    "Estado":val.get("estado"),
                    "Comentarios":val.get("comentario"),
                    "Codigo cliente":val.get("codigo_cliente")
                })
    return pedidosEntregado

def menu():
    print(""" 

                                 Reporte de Pedidos
          1.Listado de los estados por los que puede pasar un pedido.
          2.Listado con el codigo de pedido, codigo de cliente,fecha esperada y fecha de entrega 
           de los pedidosentregados a tiempos.
          3. Listado con el codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega
           de los pedidos cuya fecha de entrega ha sido al menos dos dias de la fecha esperada.
          4. Listado de todos los pedidos que fueron rechazados en 2009.
          5. listado de todos los pedidos que han sido entregados en el mes de enero de cualquier año.
""")
    opcion=int(input("Ingrese el numero de la opción que desea observar : "))
    
    print()
    if opcion==1:
        print(tabulate(getAllDiferentesEstados(),headers="keys",tablefmt="github"))
    elif opcion==2:
        print(tabulate(getAllPedidosEntregadosAtrasadosdeTiempo(),headers="keys",tablefmt="github"))
    elif opcion==3:
        print(tabulate(getAllPedidosEntregadosdosdiasantesdeTiempo(),headers="keys",tablefmt="github"))
    elif opcion==4:
        print(tabulate(getAllPedidosRechazados2009(),headers="keys",tablefmt="grid", colalign=("left",)))
    elif opcion==5:
        print(tabulate(getAllPedidosEntregadosdelmesdeenero(),headers="keys",tablefmt="github"))

print()