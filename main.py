# from tabulate import tabulate
import sys 
import modules.getempleado as empleado
import modules.getclientes as clientes
import modules.getpedidos as pedidos
import modules.getpagos as pagos
import modules.getoficina as oficina
import modules.getproducto as producto
import modules.postProducto as PosP

print()

if(__name__=="__main__"):
    while True:
        print(f"""
            
            --- Menu Principal ---
            
            0. salir
            1. Clientes
            2. Empleados
            3. Oficina
            4. Pago
            5. Pedido
            6. Producto""")

        op = int(input("Ingrese opcion: "))
        if op == 1:
            clientes.menu()
        elif op == 2:
            empleado.menu()
        elif op == 3:
            oficina.menu()
        elif op == 4:
            pagos.menu()
        elif op == 5:
            pedidos.menu()
        elif op == 6:
            producto.menu()
        elif op==7:
            PosP.menu()
        elif op == 0:
            break
        
