
from src.tablaControlDni import TablaControlDni


class Dni:

    def __init__(self,cadena):
        self.dni = cadena
        self.tabla = TablaControlDni()
        self.numero_sano = False
        self.letra_sana = False

    def set_dni(self, cadena):
        self.dni = cadena

    def get_dni(self):
        return self.dni
    
    def set_numero_sano(self,valor):
        self.numero_sano = valor
    
    def get_numero_sano(self):
        return self.numero_sano  
    
    def set_letra_sana(self,valor):
        self.letra_sana = valor

    def get_letra_sana(self):
        return self.letra_sana
    
    def check_dni(self):
        self.numero_sano(self.__check_dni_lenght() and self.__check_dni_number())
        return self.get_numero_sano()
    
    def check_cif(self):
        return self.__check_dni_number and self.__check_letra()
    
    def check_letra(self):
        if self.get_numero_sano():
            self.letra_sana( self.__check_letra() and  self.__check_letra_mayuscula() and self.__check_letra_vale )
            return self.get_letra_sana()

        else:
            return False
        
    def dar_letra(self):

        if self.get_numero_sano():
            return self.tabla.calcular_resto(self.__get_parte_numerica())
        else:
            return None

    def __check_dni_lenght(self):
        return len(self.get_dni()) == 9
    
    def __check_dni_number(self):
        return self.dni[:-1].isdigit()
    
    def __check_letra(self):
        return self.__get_parte_alfabetica_dni.isalpha()

    def __get_parte_alfabetica_dni(self):
        return self.dni[-1]

    def __check_letra_mayuscula(self):
        return self.__get_parte_alfabetica_dni.isupper()
    
    def __get_parte_numerica(self):
        return self.get_dni[:-1]

    def __check_letra_vale(self):

        if self.get_numero_sano():
            return self.__get_parte_alfabetica_dni() == self.dar_letra()
    