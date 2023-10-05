
class ClaseBase:
    def __init__(self):
        self.ataque = 2
        self.armadura = 0
        self.salud = 4
    
    def habilidad_especial(self):
        pass
    
    def atacar(self, entidad):
        entidad.salud -= self.ataque
