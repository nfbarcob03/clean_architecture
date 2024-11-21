class CalculadoraDescuento: 
    def calcular(self, tipo_cliente, monto): 
        if tipo_cliente == "estudiante": 
            return monto * 0.8 # 20% de descuento 
        elif tipo_cliente == "senior": 
            return monto * 0.7 # 30% de descuento 
        elif tipo_cliente == "regular": 
            return monto * 0.9 # 10% de descuento 
        else: return monto # Sin descuento 
    # Uso 
if __name__ == "__main__": 
    calculadora = CalculadoraDescuento() 
    total = calculadora.calcular("estudiante", 100) 
    print(f"Total con descuento: {total}")