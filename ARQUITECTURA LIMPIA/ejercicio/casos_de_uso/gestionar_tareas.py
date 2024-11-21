import json 
import os 
from entidades.tarea import Tarea 
class GestionarTareas: 
    def __init__(self, archivo_tareas='tareas.json'): 
        self.archivo_tareas = archivo_tareas 
        self.tareas = self.cargar_tareas() 
        self.siguiente_id = max([t.id_tarea for t in self.tareas], default=0) + 1 
    def cargar_tareas(self): 
        if not os.path.exists(self.archivo_tareas): 
            return []
        with open(self.archivo_tareas, 'r') as file: 
            tareas_dict = json.load(file) 
            return [Tarea.from_dict(t) for t in tareas_dict] 
    def guardar_tareas(self): 
        with open(self.archivo_tareas, 'w') as file: 
            tareas_dict = [tarea.to_dict() for tarea in self.tareas] 
            json.dump(tareas_dict, file, indent=4) 
    def crear_tarea(self, titulo: str, descripcion: str):
        tarea = Tarea(self.siguiente_id, titulo, descripcion) 
        self.tareas.append(tarea) 
        self.siguiente_id += 1 
        self.guardar_tareas() 
        return tarea 
    def listar_tareas(self): 
        return self.tareas 
    def completar_tarea(self, id_tarea: int): 
        for tarea in self.tareas: 
            if tarea.id_tarea == id_tarea: 
                tarea.marcar_completada() 
                self.guardar_tareas() 
                return tarea 
        return None