class Tarea: 
    def __init__(self, descripcion): 
        self.descripcion = descripcion 
        self.completada = False 
        
    def completar(self): 
        self.completada = True