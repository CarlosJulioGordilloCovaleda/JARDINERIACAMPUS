import requests

# "http://154.38.171.54:5004/gama" Enlace Profe
def getAllgamas():  
    peticion=requests.get("http://154.38.171.54:5004/gama")
    data=peticion.json()
    return data
# Sacar el Menu de las gamas
def getNombresGammas():
    data=[]
    for val in getAllgamas():
        data.append(val.get("gama"))
    return data

def getNombresGamma(gama):
    for val in getAllgamas():
        if (val.get("gama")==gama):
            return[val]

