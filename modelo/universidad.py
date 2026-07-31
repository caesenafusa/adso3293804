from curso import curso
class universidad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.cursos=[]
    def crear_curso(self,nombre):
        curso_nuevo=curso(nombre)
        self.cursos.append(curso_nuevo)
    def crear_curso2(self):
         name=input("diga el nombre del curso")
         curso_nuevo=curso(name)
         self.cursos.append(curso_nuevo)
    def matricular(self,estudiante,curso):
        for c in self.cursos:
                if c.get_nombre_curso()==curso:
                    c.vincular_estudiante(estudiante)
                    print('proceso exitoso')
    def lista_estudiantes(self,curso):
            for c in self.cursos:
                if c.get_nombre_curso()==curso:
                     c.get_estudiantes()


