class profesor:
    def __init__(self, nombre,asignatura):
        self.nombre=nombre        
        self.asignatura=asignatura
    def datos_profesor(self):
        return (f"nombre: {self.nombre} asignatura: {self.asignatura}")
