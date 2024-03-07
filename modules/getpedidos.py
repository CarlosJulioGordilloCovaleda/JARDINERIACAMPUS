import storage.pedido as pe
from datetime import datetime
#Devuelve un listado con los distintos estados por los que puede pasar un pedido
def getAllDiferentesEstados(estado):
    DiferentesEstados=set()
    for val in pe.pedido:
        if val.get("estado") != None:
            DiferentesEstados.add(val.get("estado"))
    lista_DiferentesEstados=list(DiferentesEstados)
    return lista_DiferentesEstados
# Devuelve un listado con el codigo de pedido,
#codigo de cliente,fecha esperada y fecha de entrega 
#de los pedidos que no han sido entregados a tiempos

def getAllPedidosEntregadosAtrasadosdeTiempo():
    pedidosEntregado=[]
    for val in pe.pedido:
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
                    "codigo_de_pedido":val.get("codigo_pedido"),
                    "codigo_de_cliente":val.get("codigo_cliente"),
                    "fecha_esperada":val.get("fecha_esperada"),
                    "fecha_de_entrega":val.get("fecha_entrega")
                })
    return pedidosEntregado

# Devuelve un listado con el codigo de pedido, codigo de cliente fecha esperada y fecha de entrega
#de los pedidos cuya fecha de entrega ha sidoal menos dos dias de la fecha esperada

def getAllPedidosEntregadosdosdiasantesdeTiempo():
    pedidosEntregado=[]
    for val in pe.pedido:
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
                    "codigo_de_pedido":val.get("codigo_pedido"),
                    "codigo_de_cliente":val.get("codigo_cliente"),
                    "fecha_esperada":val.get("fecha_esperada"),
                    "fecha_de_entrega":val.get("fecha_entrega")
                })
    return pedidosEntregado

#Devuelve un listado dde todos los pedidos que fueron rechazados en  2009

def getAllPedidosRechazados2009():
    pedidosEntregado=[]
    for val in pe.pedido:
        fechapedido=val.get("fecha_pedido")
        if val.get("estado")== "Rechazado" and val.get("fecha_pedido")!=None:
            fechaconvertida=datetime.strptime(fechapedido,"%Y-%m-%d")
            if fechaconvertida.year==2009:
                pedidosEntregado.append({
                    "codigo_pedido":val.get("codigo_pedido"),
                    "fecha_pedido":val.get("fecha_pedido"),
                    "fecha_esperada":val.get("fecha_esperada"),
                    "fecha_entrega":val.get("fecha_entrega"),
                    "estado":val.get("estado"),
                    "comentarios":val.get("comentario"),
                    "codigo_cliente":val.get("codigo_cliente")
                })
    return pedidosEntregado

#Deuelve un listado de todos los pedidos que han sido entregados en el mes de enero de cualquier año

def getAllPedidosEntregadosdelmesdeenero():
    pedidosEntregado=[]
    for val in pe.pedido:
        fechaEntrega=val.get("fecha_entrega")
        if val.get("estado")=="Entregado" and val.get("fecha_entrega")!=None:
            fechaconvertida=datetime.strptime(fechaEntrega,"%Y-%m-%d")
            if fechaconvertida.month==1:
                pedidosEntregado.append({
                    "codigo_pedido":val.get("codigo_pedido"),
                    "fecha_pedido":val.get("fecha_pedido"),
                    "fecha_esperada":val.get("fecha_esperada"),
                    "fecha_entrega":val.get("fecha_entrega"),
                    "estado":val.get("estado"),
                    "comentarios":val.get("comentario"),
                    "codigo_cliente":val.get("codigo_cliente")
                })
    return pedidosEntregado


                
