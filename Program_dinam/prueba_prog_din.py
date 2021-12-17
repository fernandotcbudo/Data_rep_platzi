#borracho
import random


class borracho:
    def __init__(self,nombre):
        self.nombre=nombre

class borracho_tra(borracho):
    def __init__(self,nombre):
        super().__init__(nombre)

    def camina (self):
        return random.choice([(0,5),(0,-5),(5,0),(-5,0)])




