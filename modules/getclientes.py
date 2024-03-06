import storage.cliente as cl

#Devuelve un listado con todos los nombres de los clientes españoles 


def Nombres(pais): 
    Nombres=[]
    for val in cl.clientes:
        if (val.get("pais")=="Spain"):
            Nombres.append({
                "nombre":val.get("nombre_cliente")
            }) 
    return Nombres