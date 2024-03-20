import re
import os
import requests
import modules.getgama as Ggm
from tabulate import tabulate
def PosGama():
    resultado=dict()
    while True:
        try:
            # Nombre de la gama
            if(not resultado.get("gama")):
                gama=input("Ingrese el nombre de la nueva gama: ")
                data=Ggm.getNombresGamma(gama)
                if data:
                    print(tabulate(data, headers="keys", tablefmt="github"))
                    raise Exception ("Esta gama ya existe")               
                else:
                    resultado["gama"]=gama.title()
            # Descripcion
            if(not resultado.get("descripcion_texto")):
                descrip=input("Agregue un descripción maximo de 20 caracteres : ")
                if(re.match(r'^.{1,20}$',descrip) is not None):
                    resultado["descripcion_texto"]=descrip.capitalize()
                    
                else:
                    raise Exception("La descripción supera el numero de caracteres")
            if(not(resultado.get("descripcion_html"))):
                deshtml=input("Ingrese la descripcion en HTML: ")
                if deshtml.split():
                    resultado["descripcion_html"]=deshtml.capitalize()
                else:
                    resultado["descripcion_html"]=None
            resultado["imagen"]=None
            break
        except Exception as error:
            print(error)
    print(resultado)
       



# "descripcion_texto": "Plantas para jardin decorativas",
# "descripcion_html": null,
# "imagen": null