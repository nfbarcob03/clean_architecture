Explicación de la Refactorización
1. Separación de Responsabilidades: 
• La clase Empleado ahora solo se encarga de almacenar datos relacionados con el empleado y calcular su salario total. 
• La lógica de cálculo de bonus se ha trasladado a clases específicas de Rol, lo que hace que el código sea más extensible y siga el principio de responsabilidad única. 
2. Eliminación de la Obsesión por Tipos Primitivos: 
• Se reemplazaron las cadenas que determinaban el rol con clases específicas para cada rol (Gerente, Director, EmpleadoBase). Esto hace que el código sea menos propenso a errores y más fácil de entender. 
3. Inversión de Dependencias y Persistencia: 
• La lógica para guardar empleados se ha movido a una clase RepositorioEmpleados, lo que permite cambiar la forma en que se guardan los empleados sin afectar la clase Empleado. 4
. Extensibilidad: 
• Ahora es fácil agregar nuevos roles con diferentes cálculos de bonus sin modificar el código existente, solo extendiendo la clase Rol.