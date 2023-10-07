from ClaseBase import ClaseBase

# TODO: Generar un sistema para que los ataques puedan afectar a una lista de Entidades

class Mago(ClaseBase):
    def __init__(self):
        self.ataque = 1
        self.armadura = 0            
        self.salud = 5
        self.habilidad_especial_usos = 3

    def mensaje_hechizo(func):
        def wrapper(self, entidad):
            print(f"¡Lanzas un hechizo a {entidad.nombre}! Infligiste {self.ataque * 2} de daño.")
            func(self, entidad)
        return wrapper

    @mensaje_hechizo
    def hechizo_ataque(self, entidad):
        entidad.salud -= self.ataque * 2

    def mensaje_ataque(func):
        def wrapper(self, entidad):
            print(f"¡Atacas a tu enemigo con tu bastón! inflingiste {self.ataque}. de daño a {entidad.nombre}")
            func(self, entidad)
        return wrapper

    @mensaje_ataque
    def atacar(self, entidad):
        super().atacar(entidad)  # call the atacar() method of the parent class

    def habilidad_especial(self, entidad, hechizo):
        if self.habilidad_especial_usos > 0:
            self.hechizo(entidad)
            self.habilidad_especial_usos -= 1
            print(f"Te quedan {self.habilidad_especial_usos} usos de habilidad especial.")
        else:
            print("No te quedan usos de habilidad especial.")
    