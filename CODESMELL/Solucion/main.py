from empleado import Empleado 
from roles import Gerente, Director, EmpleadoBase 
from repositorio_empleados import RepositorioEmpleados 
def main(): 
    # Crear instancias de roles 
    rol_gerente = Gerente() 
    rol_director = Director() 
    rol_empleado_base = EmpleadoBase() 
    # Crear instancias de empleados con diferentes roles 
    empleado_1 = Empleado("Carlos Perez", 5000, rol_gerente) 
    empleado_2 = Empleado("Ana Gomez", 7000, rol_director) 
    empleado_3 = Empleado("Juan Ruiz", 3000, rol_empleado_base) 
    # Calcular y mostrar salarios 
    for empleado in [empleado_1, empleado_2, empleado_3]: 
        salario_total = empleado.obtener_salario_total() 
        print(f"Salario total de {empleado.nombre}: {salario_total}") 
    
    # Guardar empleados en la base de datos 
    repositorio = RepositorioEmpleados() 
    for empleado in [empleado_1, empleado_2, empleado_3]: 
        repositorio.guardar(empleado)

if __name__ == "__main__": main()