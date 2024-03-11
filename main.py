# from tabulate import tabulate
import modules.getempleado as empleado
import modules.getclientes as clientes
import modules.getpedidos as pedidos
import modules.getpagos as pagos
import modules.getoficina as oficina
import modules.getproducto as producto
import sys
#print(empleado.getAllPuestoNombreApellidosEmail(None))

#print(empleado.getNombreApellidosPuesto("Representante Ventas"))
print()
#print(clientes.Nombres("pais"))
#print(pedidos.getAllDiferentesEstados("estado"))
#print(pagos.getCodigosClientes2008("codigo_cliente"))
#print(pedidos.getAllPedidosEntregadosAtrasadosdeTiempo())
#print(tabulate(pedidos.getAllPedidosEntregadosdosdiasantesdeTiempo(),tablefmt="grid"))
#print(tabulate(pedidos.getAllPedidosRechazados2009(),tablefmt="grid"))
#print(tabulate(pedidos.getAllPedidosEntregadosdelmesdeenero(),tablefmt="grid"))
#print(tabulate(pagos.getAllPagos2008Paypal(),tablefmt="grid"))
 
def menu():
    print(f"""
          
        --- Menu Principal ---
        
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
           
menu()
