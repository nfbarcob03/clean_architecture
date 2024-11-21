from descuento import Descuento 
class DescuentoSenior(Descuento): 
    def aplicar_descuento(self, monto): 
        return monto * 0.7 # 30% de descuento