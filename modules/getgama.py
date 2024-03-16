import requests

#"http://192.168.1.16:5020" gama_producto.json
def getAllgamas(gama):
    peticion=requests.get("http://192.168.1.16:5020")
    data=peticion.json()
    return data
