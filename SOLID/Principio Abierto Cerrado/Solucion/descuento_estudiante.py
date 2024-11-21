from descuento import Descuento 
class DescuentoEstudiante(Descuento): 
    def aplicar_descuento(self, monto): 
        return monto * 0.8 # 20% de descuento