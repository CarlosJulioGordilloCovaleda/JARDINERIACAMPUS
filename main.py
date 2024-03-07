from tabulate import tabulate
import modules.getempleado as empleado
import modules.getclientes as clientes
import modules.getpedidos as pedidos
import modules.getpagos as pagos
import datetime
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
print(tabulate(pagos.getAllPagos2008Paypal(),tablefmt="grid"))