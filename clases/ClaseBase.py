
class ClaseBase:
    def __init__(self):
        self.ataque = 2
        self.armadura = 0
        self.salud = 4

    def habilidad_especial(self):
        pass
    
    def mensaje_ataque(func):
        def wrapper(self, entidad):
            print(f"¡Atacas a tu enemigo con tus manos! inflingiste {self.ataque}. de daño a {entidad.nombre}")
            func(self, entidad)
        return wrapper
    
    @mensaje_ataque
    def atacar(self, entidad):
        entidad.salud -= self.ataque
