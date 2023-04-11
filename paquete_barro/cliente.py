from datetime import datetime

class Cliente:

    # Constructor
    def __init__(self, nombre, apellido, dni, nacimiento, direccion, usuario, clave, compras):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.nacimiento = nacimiento
        self.direccion = direccion
        self.usuario = usuario
        self.clave = clave
        self.compras = compras

    def __str__(self):
        return f"NOMBRE: {self.nombre}, APELLIDO: {self.apellido}, DNI: {self.dni}, NACIMIENTO: {self.nacimiento}, USUARIO: {self.usuario}, CLAVE: {self.clave}"
    
    # Muestra el item que compra el cliente y lo almaceno
    def comprar (self, item, precio, local):
        my_key = f"compra{len(self.compras)}"
        self.compras.update({ my_key : {"item": item, "precio": precio, "local": local} })
        print(f"\033[1;32mEl cliente {self.nombre.upper()} {self.apellido.upper()} ha comprado {item.upper()} por $ {precio} del local {local.upper()}\033[0m\n")

    # Muestra el nombre completo del cliente
    def getNombreCompleto (self):
        print(f"El cliente se llama {self.apellido.upper()}, {self.nombre.upper()}")
    
    # Muestra la edad que tiene el cliente
    def getEdad (self):
        # Convertir la fecha a objeto datetime
        fecha_nacimiento = datetime.strptime(self.nacimiento, '%d/%m/%Y')
        
        # Obtener la fecha actual
        hoy = datetime.now()

        # Se hace el cálculo de la edad en años
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        print(f"El cliente tiene {edad} años")
 
    # Actualizar la dirección del cliente por una nueva
    def update_direccion (self, nueva_direccion):
        print(f"La dirección de {self.nombre} {self.apellido} ha sido actualizada a {nueva_direccion}")
        self.direccion = nueva_direccion