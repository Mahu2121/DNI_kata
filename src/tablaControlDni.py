

class TablaControlDni:

    def __init__(self):
        self.letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E",]

    def get_letras(self):
        return self.letras 
    
    def get_letra(self,posicion):
        try:
            return self.letras[posicion]
        except IndexError:
            return "Posicion letra fuera de rango"
    
    def get_modulo(self):
        return len(self.get_letras())
    
    def is_letra_permitida(self,letra):

        return letra in self.get_letras()
    
    def calcular_resto(self,dni):

        posicion = int(dni) % self.get_modulo()
        return self.get_letra(posicion)

        

