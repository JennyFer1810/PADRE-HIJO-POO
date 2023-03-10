from padre import Persona
from padre import Persona2
from madre import Madre
from padre import Padre

class Hijo3(Persona):
    vivienda = str
    
    def __init__(self, nombre, apellido, edad, vivienda):
        super().__init__(nombre, apellido, edad)
        self.vivienda = vivienda
        
hijo3  = Hijo3("Diego", "Yanez", 29, "Centro")
padre3 = Persona("German", "Yanez", 50)

print(vars(hijo3))
print(vars(padre3))
print(hijo3.conversar(padre3))

class Hijo4(Persona2):
    edad     = int
    semestre = str
    
    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad
        self.semestre = semestre
        
    def felicitar(self,padre):
        return f"Felicidades {self.nombre}, acabas de termiar tu  {self.semestre}, a tus {self.edad} att {padre4.nombre} {padre.apellido}"
    
padre4 = Persona2("Dilan", "Bonilla")
hijo4  = Hijo4("Daniel", "Bonilla", 20, "Segundo")

print(vars(padre4))
print(vars(hijo4))
print(hijo4.felicitar(padre4))

class Hijofinal(Padre, Madre):
    nombre          = str
    apellidoPaterno = str
    apellidoMaterno = str
    apellido        = str
    padre           = Padre("", "", "", "")
    madre           = Madre("", "", "", "")
    
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, ciudad, apellido, madre, padre):
        super().__init__(nombre, apellido, edad, ciudad)
        self.apellidoMaterno = apellidoMaterno
        self.apellidoPaterno = apellidoPaterno
        self.madre           = madre
        self.padre           = padre
        self.apellido        = apellido       
        
padrefinal = Padre("Jonathan", "Diaz", 30, "Machala")
madrefinal = Madre("Jennyfer", "Chalacan", 31, "Quito")
hijofinal  = Hijofinal("Andres", "Diaz", "Chalacan", 12, "Quito", "Diaz", Padre("Jonathan", "Diaz", 30, "Machala"), Madre("Jennyfer", "Chalacan", 31, "Quito"))

print(vars(padrefinal))
print(vars(madrefinal))
print(vars(hijofinal))

# print(vars(Hijofinal))
# print(vars(Hijofinal.madre))