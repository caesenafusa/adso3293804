class curso:
    def __init__(self,nombre):
        self.nombre=nombre
        self.estudiantes=[]
    def vincular_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
    def get_nombre_curso(self):
        return self.nombre
    def get_estudiantes(self):
        for e in self.estudiantes:
            print(e.get_nombre_estudiante())