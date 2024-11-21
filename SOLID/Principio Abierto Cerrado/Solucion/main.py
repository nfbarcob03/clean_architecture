from calculadora_descuento import CalculadoraDescuento 
from descuento_estudiante import DescuentoEstudiante 
from descuento_senior import DescuentoSenior 
from descuento_regular import DescuentoRegular 
# Uso 
if __name__ == "__main__": 
    calculadora_estudiante = CalculadoraDescuento(DescuentoEstudiante()) 
    total_estudiante = calculadora_estudiante.calcular(100) 
    print(f"Total con descuento para estudiante: {total_estudiante}") 
    calculadora_senior = CalculadoraDescuento(DescuentoSenior()) 
    total_senior = calculadora_senior.calcular(100) 
    print(f"Total con descuento para senior: {total_senior}") 
    calculadora_regular = CalculadoraDescuento(DescuentoRegular()) 
    total_regular = calculadora_regular.calcular(100) 
    print(f"Total con descuento para cliente regular: {total_regular}")