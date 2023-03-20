class Cliente:

    def __init__(self, nombre, apellido, usuario, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.clave = clave

    def __str__(self):
        return f"NOMBRE: {self.nombre}\nAPELLIDO: {self.apellido}\n"