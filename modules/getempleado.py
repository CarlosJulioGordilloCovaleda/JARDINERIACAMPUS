import storage.empleado as em 

#Devueelve el nombre  del puesto,nombre y apellido y emails del jefe de la empresa

def getAllPuestoNombreApellidosEmail(codigo_jefe):
    PuestoNombreApellidosEmail = []
    for val in em.empleados:
        if (val.get("codigo_jefe")==None):
            PuestoNombreApellidosEmail.append({
                "puesto":val.get("puesto"),
                "nombre":val.get("nombre"),
                "apellidos":f"{val.get('apellido1')} {val.get('apellido2')}",
                "email":val.get("email")
           }) 
            return PuestoNombreApellidosEmail

