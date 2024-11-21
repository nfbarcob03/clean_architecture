from casos_de_uso.gestionar_tareas import GestionarTareas 
class ControladorTarea: 
    def __init__(self): 
        self.gestionar_tareas = GestionarTareas() 
    def crear_tarea(self, titulo: str, descripcion: str): 
        return self.gestionar_tareas.crear_tarea(titulo, descripcion) 
    def listar_tareas(self): 
        return self.gestionar_tareas.listar_tareas() 
    def completar_tarea(self, id_tarea: int): 
        return self.gestionar_tareas.completar_tarea(id_tarea)