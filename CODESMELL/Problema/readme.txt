Código Oloroso en el código de ejemplo 
1. God Class (Clase Dios): 
• La clase Empleado tiene demasiadas responsabilidades: calcula el salario, imprime detalles y guarda en la base de datos. Esto viola el Principio de Responsabilidad Única (SRP). 
• Cuando una clase hace “demasiado”, se vuelve difícil de mantener y extender, ya que cualquier cambio podría afectar múltiples funcionalidades. 
2. Primitive Obsession (Obsesión por Tipos Primitivos): 
• En el método calcular_salario, se está usando el nombre del empleado para determinar el rol (gerente, director, etc.), lo cual es una dependencia poco fiable en lugar de tener una estructura más clara como una jerarquía de clases o un campo específico para el rol. 
• El uso de cadenas para roles puede llevar a errores difíciles de rastrear y es propenso a fallos. 
3. Long Method (Método Largo):
• El método calcular_salario realiza múltiples tareas: determina el rol y calcula el bonus. Este método podría dividirse en métodos más pequeños y específicos. 
• Métodos largos son difíciles de leer y mantener, y tienden a ocultar errores. 
4. Feature Envy (Envidia de Funcionalidad): 
• El método guardar_en_base_de_datos dentro de la clase Empleado se preocupa por detalles que deberían pertenecer a otra clase o módulo (por ejemplo, un repositorio o servicio de persistencia). 
• Esto hace que la clase Empleado dependa de funcionalidades que no deberían ser su responsabilidad. 
5. Inappropriate Intimacy (Intimidad Inapropiada): 
• La clase Empleado tiene conocimiento de cómo guardar datos en la base de datos, lo que debería estar encapsulado en otra clase. Esto crea una dependencia innecesaria y complica la prueba y mantenimiento del código.