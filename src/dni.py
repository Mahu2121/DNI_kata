
from tablaControlDni import TablaControlDni


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
        

    