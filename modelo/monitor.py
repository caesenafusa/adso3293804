from profesor import profesor
class monitor(profesor):
    def __init__(self, nombre, asignatura,semestre):
        super().__init__(nombre, asignatura)
        self.semestre=semestre
    def datos_profesor(self):
            return (f"nombre: {self.nombre} asignatura: {self.asignatura} semestre={self.semestre}")
    def remanente_estudios(self):
         return 10-self.semestre