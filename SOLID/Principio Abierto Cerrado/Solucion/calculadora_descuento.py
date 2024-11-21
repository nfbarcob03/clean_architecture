class CalculadoraDescuento: 
    def __init__(self, descuento): 
        self.descuento = descuento 
    def calcular(self, monto): 
        return self.descuento.aplicar_descuento(monto)