from paquete_barro.cliente import Cliente
from paquete_barro.product import Product
import datetime
import json

class Menu:
    def __init__(self, bd):
        self.choices = {
            "1": self.agregar_cliente,
            "2": self.mostrar_clientes,
            "3": self.realizar_compra,
            "4": self.salir
        }
        self.clientes = []
        self.bd = bd
        self.productos = []

    def display_menu(self):
        print("\033[1;32m****** MENÚ ******\033[0m")
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Realizar compra")
        print("4. Salir")

    def run(self):
        if not self.clientes:
            self.levantar_clientes(self.bd.leer_base())
            self.levantar_productos()
        
        while True:
            self.display_menu()
            choice = input("Selecciona una opción (1-4): ")
            action = self.choices.get(choice)
            if action:
                if choice >= "3":
                    action()
                    break
                else:
                    action()
            else:
                print("\033[1;31mOpción inválida, por favor selecciona una opción válida\033[0m")

    def levantar_clientes(self, base):
        for key, value in base.items():
            cliente = Cliente (value["nombre"], 
                                value["apellido"], 
                                value["dni"], 
                                value["nacimiento"], 
                                value["direccion"], 
                                key, 
                                value["clave"], 
                                value["compras"]
                                )
            self.clientes.append(cliente)

    def levantar_productos(self):

        try:
            with open("base/productos.json", "r") as f:
                bd_productos = json.load(f)
        except FileNotFoundError:
            print("Error: El archivo de productos no existe")

        for item in bd_productos:
            for key, value in item.items():
                producto = Product(key, 
                                    value["item"],
                                    value["precio"],
                                    value["local"],
                                    value["stock"])
                self.productos.append(producto)

    def agregar_cliente(self):
        while True:
            try:
                nombre = input('Ingrese Nombre: ')
        
                ## Hago múltiples validaciones al NOMBRE
                if not nombre:
                    raise ValueError("\033[1;31m** ERROR: el NOMBRE no puede ser vacío **\x1b[0m")
                elif len(nombre) < 4:
                    raise ValueError("\033[1;31m** ERROR: el NOMBRE debe tener 4 o más caracteres **\x1b[0m")
                else:
                    break
            except ValueError as e:
                print(e)

        while True:
            try:
                apellido = input('Ingrese Apellido: ')
        
                ## Hago múltiples validaciones al APELLIDO
                if not apellido:
                    raise ValueError("\033[1;31m** ERROR: el APELLIDO no puede ser vacío **\x1b[0m")
                elif len(apellido) < 4:
                    raise ValueError("\033[1;31m** ERROR: el APELLIDO debe tener 4 o más caracteres **\x1b[0m")
                else:
                    break
            except ValueError as e:
                print(e)

        while True:
            try:
                dni = input('Ingrese DNI: ').replace(" ", "")
        
                ## Hago múltiples validaciones al DNI
                if not dni.isdigit():
                    raise ValueError("\033[1;31m** ERROR: el DNI debe consistir en números **\x1b[0m")
                elif not dni:
                    raise ValueError("\033[1;31m** ERROR: el DNI no puede ser vacío **\x1b[0m")
                elif len(dni) < 7 or len(dni) > 8:
                    raise ValueError("\033[1;31m** ERROR: el DNI debe tener 7 u 8 dígitos **\x1b[0m")
                else:
                    break
            except ValueError as e:
                print(e)

        while True:
            try:
                nacimiento = input('Ingrese Fecha de nacimiento (DD/MM/YYYY): ').replace(" ", "")
                fecha_nacimiento = datetime.datetime.strptime(nacimiento, "%d/%m/%Y")
                
                ## Hago múltiples validaciones a la FECHA DE NACIMIENTO
                if nacimiento != fecha_nacimiento.strftime("%d/%m/%Y"):
                    raise ValueError("\033[1;31m** ERROR: la FECHA DE NACIMIENTO debe tener el formato DD/MM/YYYY **\x1b[0m")
                elif not nacimiento:
                    raise ValueError("\033[1;31m** ERROR: la FECHA DE NACIMIENTO no puede ser vacío **\x1b[0m")
                elif len(nacimiento) != 10:
                    raise ValueError("\033[1;31m** ERROR: la FECHA DE NACIMIENTO debe tener 10 caracteres **\x1b[0m")
                else:
                    break
            except ValueError as e:
                if "does not match format" in str(e):
                    print("\033[1;31m** ERROR: la FECHA DE NACIMIENTO no tiene el formato DD/MM/YYYY **\x1b[0m")
                else:
                    print(e)

        while True:
            try:
                direccion = input('Ingrese Dirección: ')
        
                ## Hago múltiples validaciones a la DIRECCIÓN
                if not direccion:
                    raise ValueError("\033[1;31m** ERROR: la DIRECCIÓN no puede ser vacío **\x1b[0m")
                elif len(direccion) < 4:
                    raise ValueError("\033[1;31m** ERROR: la DIRECCIÓN debe tener 10 caracteres **\x1b[0m")
                else:
                    break
            except ValueError as e:
                print(e)

        while True:
            try:
                usuario = input('Ingrese Nombre de Usuario: ').replace(" ", "")
        
                ## Hago múltiples validaciones al USUARIO
                if not usuario:
                    raise ValueError("\033[1;31m** ERROR: el USUARIO no puede ser vacío **\x1b[0m")
                elif len(usuario) < 4 or len(usuario) > 10:
                    raise ValueError("\033[1;31m** ERROR: el USUARIO debe tener entre 4 y 10 caracteres **\x1b[0m")
                elif usuario in self.clientes:
                    raise ValueError("\033[1;31m** ERROR: el USUARIO ya existe en la BD **\x1b[0m")
                else:
                    break
            except ValueError as e:
                print(e)

        while True:
            try:
                clave = input('Ingrese Contraseña: ')

                ## Hago múltiples validaciones a la CLAVE
                if not clave:
                    raise ValueError("\033[1;31m** ERROR: la CLAVE no puede ser vacía **\x1b[0m")
                elif len(clave) < 5:
                    raise ValueError("\033[1;31m** ERROR: la CLAVE debe tener mínimo 5 caracteres **\x1b[0m")
                else:
                    break
            except ValueError as e:
                print(e)

        cliente = Cliente(nombre, apellido, dni, nacimiento, direccion, usuario, clave, [])
        self.clientes.append(cliente)
        self.bd.agregar_cliente(cliente)
        

        # Pregunto si quiere seguir agregando usuarios o no para que se produzca un bucle
        while True:
            try:
                confirmacion = input('Quiere seguir agregando clientes? (S/N)').upper()
                if confirmacion == 'N':
                    print('\n\033[1;32mCLIENTE AGREGADO/S SATISFACTORIAMENTE.\033[0m')
                    self.bd.guardar_base()
                    break
                elif confirmacion == 'S':
                    self.agregar_cliente()
                    break
            except:
                pass

    def mostrar_clientes_listado(self):
        for i, cliente in enumerate(self.clientes, start=1):
                print(f"{i}. {cliente.nombre} {cliente.apellido} - DNI: {cliente.dni}")

    def mostrar_clientes(self):
        print("\n\033[1;34m****** MOSTRANDO CLIENTES ******\033[0m")
        if not self.clientes:
            print("No hay clientes registrados\n\n")
        else:
            self.mostrar_clientes_listado()

    def realizar_compra(self):
        print("\n\033[1;35m****** SELECCIONE UN CLIENTE ******\033[0m")
        if not self.clientes:
            print("No hay clientes registrados\n\n")
        else:
            self.mostrar_clientes_listado()
            
            while True:
                choice = input(f"Selecciona un cliente (1-{len(self.clientes)}): ")
                if choice:
                    if int(choice) > 0 and int(choice) <= len(self.clientes):
                        print("\033[1;35m****** SELECCIONE UN PRODUCTO ******\033[0m")
                        
                        for i, producto in enumerate(self.productos, start=1):
                            print(f"{i}. {producto.item} ($ {producto.precio}) - {'STOCK: ' + str(producto.stock) if producto.stock > 0 else 'SIN STOCK'}")
                        
                        print(f"{len(self.productos)+1}. Volver al menú")

                        while True:
                            choice2 = input(f"Selecciona una opción (1-{len(self.productos)+1}): ")
                            num = int(choice2)-1
                            if choice2:
                                if int(choice2) == len(self.productos)+1:
                                    self.run()
                                    break
                                elif int(choice2) > 0 and int(choice2) < 6 and self.productos[num].stock > 0:
                                    self.clientes[int(choice)-1].comprar(self.productos[num].item, self.productos[num].precio, self.productos[num].local)
                                    # Agrego la modificación a memoria
                                    self.bd.agregar_cliente(self.clientes[int(choice)-1])
                                    # Guardo todo en la base
                                    self.bd.guardar_base()
                                    # Bajo el stock
                                    self.productos[num].stock -= 1
                                    data = [producto.to_dict() for producto in self.productos]

                                    with open("base/productos.json", "w") as datos:
                                        json.dump(data, datos, indent=4)  

                                    # Vuelvo a mostrar el menú principal
                                    self.run()
                                    break
                                elif self.productos[num].stock == 0:
                                    print("\033[1;31mDebe elegir un producto que posea stock\033[0m")
                            else:
                                print("\033[1;31mOpción inválida, por favor selecciona una opción válida\033[0m")

                        break
                else:
                    print("\033[1;31mOpción inválida, por favor selecciona una opción válida\033[0m")

    def salir(self):
        self.bd.cerrar_base()