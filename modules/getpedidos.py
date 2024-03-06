import storage.pedido as pe
#Devuelve un listado con los distintos estados por los que puede pasar un pedido
def getAllDiferentesEstados(estado):
    DiferentesEstados=set()
    for val in pe.pedido:
        if val.get("estado") != None:
            DiferentesEstados.add(val.get("estado"))
    lista_DiferentesEstados=list(DiferentesEstados)
    return lista_DiferentesEstados

