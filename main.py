# from tabulate import tabulate
import os
import sys 
import re

from click import clear
import modules.getempleado as empleado
import modules.getclientes as clientes
import modules.getpedidos as pedidos
import modules.getpagos as pagos
import modules.getoficina as oficina
import modules.getproducto as producto
import modules.postProducto as PosP
import modules.getgama as gG

PosP.postProducto()
#print(producto.getNombresProveedores())

# if(__name__=="__main__"):
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
        

        
        
       
       
