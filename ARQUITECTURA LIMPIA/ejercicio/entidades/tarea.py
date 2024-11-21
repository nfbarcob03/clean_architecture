from datetime import datetime 
class Tarea: 
    def __init__(self, id_tarea: int, titulo: str, descripcion: str, completada: bool = False): 
        self.id_tarea = id_tarea 
        self.titulo = titulo
        self.descripcion = descripcion 
        self.completada = completada 
        self.fecha_creacion = datetime.now() 

    def marcar_completada(self): 
        self.completada = True 

    def __str__(self): 
        estado = "Completada" if self.completada else "Pendiente" 
        return f"Tarea {self.id_tarea}: {self.titulo} - {estado}" 
        
    @staticmethod 
    def from_dict(tarea_dict): 
        return Tarea( id_tarea=tarea_dict['id_tarea'], titulo=tarea_dict['titulo'], descripcion=tarea_dict['descripcion'], completada=tarea_dict['completada'] ) 
    
    def to_dict(self): 
        return { 'id_tarea': self.id_tarea, 'titulo': self.titulo, 'descripcion': self.descripcion, 'completada': self.completada }