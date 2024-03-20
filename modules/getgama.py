import requests

#"http://192.168.1.16:5020" gama_producto.json
def getAllgamas():
    peticion=requests.get("http://172.16.106.118:5020")
    data=peticion.json()
    return data

def getNombresGamma(gama):
    for val in getAllgamas():
        if (val.get("gama")==gama):
            return[val]

