import datetime
import storage.pago as pg
#Devuelve un listado con el codigo de cliente de aquello clientes
#que realizaron algun pago en 2008 tenga en cuenta que debera
#Eliminaraquellos codigos de cliente que aparezcan repetidos

def getCodigosClientes2008(codigo_cliente):
    CodigosClientes2008=set()
    for val in pg.pago:
        fechaPago=(val.get("fecha_pago"))
        if fechaPago!=None:
            fechaPagoConvertida=datetime.datetime.strptime(fechaPago,"%Y-%m-%d")
            if fechaPagoConvertida.year==2008:
                CodigosClientes2008.add(val.get("codigo_cliente"))
    listaDeCodigos2008=list(CodigosClientes2008)
    return listaDeCodigos2008


        
