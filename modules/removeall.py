import requests

def Producto():
    # listID = []
    # # for val in data.Producto():
    # #     listID.append(val.get("id"))
        
    # if id in listID:
    id = "af4e"
    requests.delete(f"http://154.38.171.54:5008/productos/{id}")
    print("Producto eliminado")
    
Producto()

# import requests
# import modules.getAllData as data


# def Pago(id):
#     listID = []
#     for val in data.Pago():
#         listID.append(val.get("id"))
        
#     if id in listID:
#         requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
#         print("Pago eliminado")
#     else:
#         print("Error, este Pago no existe !")
