# el disparador puede ser que se quiera que una clase solo tenga una instancia
# y que se este guardando en una variable todo el tiempo

class Calculadora():
    __instance = None # Atributo de clase donde se almacenará la instancia única

    def __new__(cls):
        if Calculadora.__instance is None:
            Calculadora.__instance = object.__new__(cls) # Se crea la instancia
            
        return Calculadora.__instance

    def __init__(self):
        # tengo que chequear si ya se inicializó
        if not hasattr(self, '__valor'):
            self.__valor = 0

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor
