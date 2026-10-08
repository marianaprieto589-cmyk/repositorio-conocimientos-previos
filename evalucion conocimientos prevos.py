class persona:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero =genero


class Estudiante:
            def __init__(self, nombre, genero, materia, nota):
                self.nombre = nombre
                self.genero =genero
                self.materia = materia
                self.nota =nota



def ContarRegulares(self):
    print ("nombre:",self.nombre)
    print ("genero:", self.genero)
    print ("materia:",self.materia)
    
    if self.nota >= 2.5:
        print ("Promedio regular")
        
 
Marcela = Estudiante ("Marcela", "Femenino", "matematicas", 2.5)
   
self.ContarRegulares()