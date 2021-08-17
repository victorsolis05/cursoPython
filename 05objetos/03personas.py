#Vamos a definir un objeto persona, le vamos a calcular si IMC


class Persona():
    #aqui puede ir toto el codigo python que necesitemos
    contador = 0
    def __init__(self, nombre, altura, peso):
        self.__nombre = nombre #private
        self.__altura = altura #private
        self.__peso = peso
        Persona.contador +=1
        self.__imc = peso / (altura * altura)

    def describirPersona(self):
        return f'''
        La pesona se llama: {self.__nombre} 
        Altura: {self.__altura}
        Peso: {self.__peso}
        IMC: {self.__imc}
        '''
    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def imc(self):
        return self.__imc
    

    def __eq__(self, other) -> bool:
        if not isinstance(other, Persona):
            return False
        return self.__altura == other.altura and self.__nombre == other.nombre and self.__peso == other.peso

    
    def __repr__(self) -> str:
        # print(persona1) -> Esto funiona si solo tines __repr__ en tu objeto
        #si tienes repr y str, entonces
        #para ver este contenido necesitas la funcion repr
        #print(repr(persona1)) -> Esto es cuando tienes __repr__  como __str__ en tu objeto
        return f"La persona {self.__nombre}"


    def __str__(self) -> str:
        #print(persona1)
        return f'''
        La pesona se llama: {self.__nombre} 
        Altura: {self.__altura}
        Peso: {self.__peso}
        IMC: {self.__imc}
        '''


persona1 = Persona("Jose", 1.80, 85)
persona2 = Persona("Manuel", 1.80, 80)
persona3 = Persona("Victor", 1.87, 95)

print(persona1)
print(repr(persona1))
print(persona1 == persona1)

print(persona3.contador)
#print(persona3.__altura) #error
print(persona3.altura)
#print(persona3.describirPersona())
persona3.altura = 1.60
print(persona3.altura)