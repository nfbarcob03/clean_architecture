from app.modelo import Tarea 
class GestorTareas: 
    def __init__(self): 
        self.tareas = [] 
    
    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion) 
        self.tareas.append(tarea) 
        return tarea 
    
    def listar_tareas_pendientes(self): 
        return [tarea for tarea in self.tareas if not tarea.completada] 
    
    def listar_tareas_completadas(self): 
        return [tarea for tarea in self.tareas if tarea.completada] 
    
    def completar_tarea(self, tarea): 
        tarea.completar()