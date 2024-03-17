import os
import re
from tabulate import tabulate 
import json
import requests
import modules.getproducto as gP
import modules.getgama as gG

def postProducto():    
    producto=dict()
    while True:
        try:
            #Para agregar el codigo del producto
            if(not producto.get("codigo_producto")):
                codigo=input(" Ingrese el codigo del producto en formato (##-XXX): ")
                if (re.match(r'^[A-Z]{2}-[0-9]{3}$',codigo) is not None):
                    data=gP.getProductosCodigo(codigo)
                    if (data):
                        print(tabulate(data,headers="keys",tablefmt="github"))
                        raise Exception("El codigo del producto ya existe")
                    else:
                        producto["codigo_producto"]=codigo
                else:
                    raise Exception("El Codigo del producto no cumple con el estandar establecido")
            # Nombre del Producto
            if(not producto.get("nombre")):
                nombre=input("Ingrese el nombre del producto en formato la primera letra de cada palabra en MAYUSCULA: ")
                if (re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$',nombre)is not None):
                    producto["nombre"]=nombre  
                else:
                    raise Exception("El nombre del producto no cumple con el estandar establecido")
            #"Gama del Producto"
            if(not producto.get("gama")):
                print("lista de gamas")
                for i,val in enumerate(gG.getNombresGamma(),start=1):
                    print(f'\t{i} {val}')
                opcion_seleccionada=(input("Selecciona una gama : "))
                if ((re.match(r'[1-5]+$',opcion_seleccionada) is not None)): # la opccion seleccionada debe estar entre 1  y 5 Expresion Regular
                    opcion_seleccionada=int(opcion_seleccionada)
                    producto["gama"]=gG.getNombresGamma()[opcion_seleccionada-1]
                else:
                    raise Exception ("El valor ingresado no corresponde a ninguna de las opciones, si desea ingresar una nueva gama debe hacerlo en el modulo de gamas")
                #return nombre_gama_seleccionado    
            #Dimensiones del producto
            if(not producto.get("dimensiones")):
                dimensiones=input("Ingrese las dimensiones del producto en el siguiente formato (#-#) ")
                if((re.match(r'^\d+-\d+$',dimensiones)is not None)):#  Expresion regular hace que hay un numero de con cualquier contidad de digitos un guion que los separa y otro numero de cualquier cantidad de digitios
                    dimensiones_espacio=dimensiones.replace('-',' - ') #Replace sirve para que el guion que se agrego en la expresion regular anteior se cambie por un guion con espacios que es tal y como esta en la base de datos esta llave de dimensiones
                    producto["dimensiones"]=dimensiones_espacio
                else:   
                    raise Exception ("Las dimensiones ingresadas no cumplen con el estandar establecido")
            # Proveedores
            if(not producto.get("proveedores")):
                print("lista de Proveedores")
                for i,val in enumerate(gP.getNombresProveedores(),start=1):
                    print(f'\t{i} {val}')
                opseleccionada=input("Ingresa el numero del proveedor: ")
                if((re.match(r'[1-8]+$',opseleccionada) is not None)): # Expresion regular sirve para seleccionar cualquier  numero del 1 al 8 
                    opseleccionada=int(opseleccionada)
                    producto["proveedores"]=gP.getNombresProveedores()[opseleccionada-1]
                else:
                    raise Exception ("El proveedor no se encuentra en la base de datos,si desea agregar un nuevo proveedor debe registrarlo en el modulo proveedores")
             # Descripción 
            if(not producto.get("descripcion")):
                descrip=input(" Ingrese la descrpción del producto debe ser mayor a 10 caracteres : ")
                if((re.match(r'^[\w\s]{10,}$',descrip) is not None)): # Con esta expresión regular, garantizamos que la descripción deba ser de al menos 10 caracteres.
                    producto["descripcion"]=descrip.capitalize()
                else:
                    raise Exception ("Formato invalido! RECUERDE la descripción debe tener al menos 10 caracteres")
            # Cantidad en stock
            if(not producto.get("cantidad_en_stock")):
                stock=input("Ingrese las unidades adquiridas : ")
                if stock.isdigit():
                    stock=int(stock)
                    if stock>=0:
                        producto["cantidad_en_stock"]=stock
                        
                    else:
                        raise Exception ("Ingrese un numero Entero")
                else:
                    raise Exception ("Dato invalido,ingrese un numero entero")
            # Precio_proveedor
            if(not producto.get("precio_proveedor")):
                pProveedor=input("Ingrese el precio de compra : ")
                if pProveedor.isdigit():
                    pProveedor=int(pProveedor)
                    if pProveedor>0:
                        producto["precio_proveedor"]=pProveedor
                        
                    else:
                        raise Exception ("Ingrese un numero entero mayor a 0")
                else:
                    raise Exception ("Dato invalido debe ingresar un numero entero")
            # Precio_venta
            if(not producto.get("precio_venta")):
                pVenta=input("Ingrese el precio de venta : ")
                if pVenta.isdigit():
                    pVenta=int(pVenta)
                    if pVenta>producto["precio_proveedor"]:
                        producto["precio_venta"]=pVenta
                        
                    else:
                        raise Exception ("Cuidado estas ingresando un precio menor al de compra")
                else:
                    raise Exception ("Dato invalido debe ingresar un numero")
            
            if producto.get("precio_proveedor"): # Esto hace que el precio proveedor aparezca de ultimo tal y como  en el archivo producto.json
                precio_proveedor = producto.pop("precio_proveedor")
                producto["precio_proveedor"]=precio_proveedor
                break

        except Exception as error:
            print(error)
    print(producto)

    peticion=requests.post ("http://192.168.1.16:5021",data=json.dumps(producto, indent=4).encode("UTF-8")) 
    res=peticion.json()
    res["Mensaje"]="Producto Guardado"
    return[res]

def menu():
    while True:
        os.system("cls")#Sirve para borrar el menu anteior seleccionado y no se haga un monton de informacion
        print("""
             
             ---------  Administrador de productos
             1. Guardar un producto nuevo
             0. Atras 
              """)
        
        opcion=int(input("Seleccione unas de las opciones : " ))
        if opcion==1:
            print(tabulate(postProducto(), headers="keys",tablefmt="github"))
            input("Presione una tecla para continuar ...")
        elif opcion==0:
            break
            