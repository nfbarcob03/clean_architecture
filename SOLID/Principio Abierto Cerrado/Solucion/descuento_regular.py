from descuento import Descuento 
class DescuentoRegular(Descuento): 
    def aplicar_descuento(self, monto): 
        return monto * 0.9 # 10% de descuento