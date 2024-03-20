# import json
# import requests
# import modules.getproducto as gP
# from tabulate import tabulate

# def updateProductoNombre(codigo):
#     while True:
#         if(codigo != None):
#             producto=gP.getProductCodigoID(codigo)
#         if(len(producto)):
#             print(tabulate(producto,headers="keys",tablefmt="github"))
#             opc=int(input("""
                  
#                   ¿Este es el producto que desea actualizar?
#                         1. si
#                         2. no
                  
#                   """))
#             if(opc):
            
#             else:
#                 codigo=None

