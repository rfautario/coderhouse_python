import json

class Base_de_datos:
    def __init__ (self, file_path):
        self.datos = None
        self.file_path = file_path
        self.leer_base()

    def leer_base (self):
        try:
            with open(self.file_path) as f:
                self.datos = json.load(f)
        except FileNotFoundError:
            print("Error: El archivo de clientes no existe")
            self.datos = {}
        
        return self.datos
    
    def agregar_cliente (self, cliente):
        new_cliente = {
                        cliente.usuario:
                            {
                            "nombre": cliente.nombre,
                            "apellido": cliente.apellido,
                            "dni": cliente.dni,
                            "nacimiento": cliente.nacimiento,
                            "direccion": cliente.direccion,
                            "clave": cliente.clave,
                            "compras": cliente.compras
                            }
                        }
        self.datos.update(new_cliente)

    def guardar_base (self):
        with open(self.file_path, "w") as datos:
            json.dump(self.datos, datos, indent=4)

    def cerrar_base (self):
        print("\n\033[1;34mGracias, hasta luego!\033[0m\n")