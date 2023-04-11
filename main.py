from paquete_barro.bd import Base_de_datos
from paquete_barro.menu import Menu

bd = Base_de_datos ("base/clientes.json")

Menu1 = Menu(bd)
Menu1.run()