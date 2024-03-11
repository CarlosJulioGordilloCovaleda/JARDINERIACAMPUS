import storage.cliente as cl
from tabulate import tabulate
# Devuelve un listado con todos los nombres de los clientes españoles


def Nombres():
    Nombres = []
    for val in cl.clientes:
        if (val.get("pais") == "Spain"):
            Nombres.append({
                "Nombre del cliente": val.get("nombre_cliente")
            })
    return Nombres


def menu():
    while True:
        print(""" 

                Reporte de los clientes
            0. Atras
            1. Obtener los nombres de los clientes Españoles
            

    """)
        print()
        opcion = int(input("Seleccione una opcion : "))
        if opcion == 1:
            print()
            print(tabulate(Nombres(), headers="keys", tablefmt="github"))
        elif opcion==0:
            break
