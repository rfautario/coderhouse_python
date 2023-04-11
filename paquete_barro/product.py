import json

class Product ():
    def __init__(self, id, item, precio, local, stock):
        self.id = id
        self.item = item
        self.precio = precio
        self.local = local
        self.stock = stock

    def leer_base (self):
        try:
            with open(self.file_path) as f:
                self.datos = json.load(f)
        except FileNotFoundError:
            print("Error: El archivo de datos no existe")
            self.datos = {}
        
        return self.datos
    
    def bajar_stock_producto (self):
        self.stock = int(self.stock)-1,

    def guardar_base (self):
        with open(self.file_path, "w") as datos:
            json.dump(self.datos, datos, indent=4)

    def to_dict(self):
        return {
            self.id: {
                "item": self.item,
                "precio": self.precio,
                "local": self.local,
                "stock": self.stock
            }
        }