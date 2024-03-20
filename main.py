# from tabulate import tabulate
import os
import sys 
import re
import json
from click import clear
import modules.getempleado as empleado
import modules.getclientes as clientes
import modules.getpedidos as pedidos
import modules.getpagos as pagos
import modules.getoficina as oficina
import modules.getproducto as producto
import modules.postProducto as PosP
import modules.getgama as gG
import modules.getclientes as cliente
import modules.postClientes as PosCl
import requests
import pycountry
from countryinfo import CountryInfo
import  modules.postPago as Pp



Pp.Pospagos() # En proceso
#PosCl.postClientes() Terminado
#PosP.postProducto() #Terminado


#if(__name__=="__main__"):    
# numero=100                          Esto hay que probarlo mejor sirve para filtar
# peticion=requests.get (f'http://172.16.106.242:5021/productos?precio_proveedor_gte={15}')
# data=peticion.json()
# print(data)
    
    #peticion = requests.get(f"http://172.16.106.242:5021/productos?codigo={codigo}")
#     while True:
#         os.system("cls")
#         print(f"""
            
           
#                 ███╗   ███╗███████╗███╗   ██╗██╗   ██╗    ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗██╗██████╗  █████╗ ██╗     
#                 ████╗ ████║██╔════╝████╗  ██║██║   ██║    ██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║██╔══██╗██╔══██╗██║     
#                 ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║    ██████╔╝██████╔╝██║██╔██╗ ██║██║     ██║██████╔╝███████║██║     
#                 ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║    ██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██║██╔═══╝ ██╔══██║██║     
#                 ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝    ██║     ██║  ██║██║██║ ╚████║╚██████╗██║██║     ██║  ██║███████╗
#                 ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝
                                                                                                          
#                     0. salir
#                     1. Clientes
#                     2. Empleados
#                     3. Oficina
#                     4. Pago
#                     5. Pedido
#                     6. Producto
              
#                   """)
            
#         op = input("Seleccione una de las siguientes opciones ")
#         if (re.match(r'[0-9]+$',op) is not None):
#                op=int(op)
#                if(op >=0 and op<=7):
#                 if op == 1:
#                     clientes.menu()
#                 elif op == 2:
#                     empleado.menu()
#                 elif op == 3:
#                     oficina.menu()
#                 elif op == 4:
#                     pagos.menu()
#                 elif op == 5:
#                     pedidos.menu()
#                 elif op == 6:
#                     producto.menu()
#                 elif op==7:
#                     PosP.menu()
#                 elif op == 0:
#                     break



## ESTO ES PARA PONER LOS ID A LOS JSON 
# with open("storage/producto.json","r") as f:
#     fichero = f.read()
#     data=json.loads(fichero)
#     for i, val in enumerate(data):
#         data[i]["id"] = (i+1)
#     data=json.dumps(data,indent=4).encode("UTF-8")
#     with open("storage/producto.json","wb+") as f1:
#         f1.write(data)
#         f1.close()




# -----------------------PRUEBAS--------------------------------
#print(clientes.obtener_provinciaspor("Spain"))
#print(cliente.codigosClientes()) #Para probar numeros de clientes
# country_info=CountryInfo("france")
# ciudades=country_info.provinces()
# print(ciudades)
#print(list(pycountry.countries))
#print(producto.getNombresProveedores())