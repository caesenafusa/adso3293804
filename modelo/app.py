from universidad import universidad
from estudiante import estudiante
u=universidad("San gabriel")
e1=estudiante("Maria")
e2=estudiante("Jose")
u.crear_curso("matematicas")
u.crear_curso("lenguaje")
u.crear_curso("biologia")
for c in u.cursos:
    print(c.get_nombre_curso())
u.matricular(e1,"lenguaje")
u.matricular(e2,"lenguaje")
u.lista_estudiantes("lenguaje")

del u
print("-"*30)
print(e1.get_nombre_estudiante())
# print("-"*30)
# for c in u.cursos:
#     print(c.get_nombre_curso())

