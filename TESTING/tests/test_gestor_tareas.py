import pytest 
import logging 
from app.gestor_tareas import GestorTareas 
# Configurar el logger 
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__) 

def test_agregar_tarea(): 
    logger.info("Iniciando test: test_agregar_tarea") 
    gestor = GestorTareas() 
    tarea = gestor.agregar_tarea("Estudiar Python") 
    logger.info(f"Tarea agregada: {tarea.descripcion}, completada: {tarea.completada}") 
    assert tarea.descripcion == "Estudiar Python" 
    assert not tarea.completada 
    logger.info("Finalizando test: test_agregar_tarea") 

def test_completar_tarea(): 
    logger.info("Iniciando test: test_completar_tarea") 
    gestor = GestorTareas()
    tarea = gestor.agregar_tarea("Estudiar Python") 
    logger.info(f"Tarea antes de completar: {tarea.descripcion}, completada: {tarea.completada}") 
    gestor.completar_tarea(tarea) 
    logger.info(f"Tarea despus de completar: {tarea.descripcion}, completada: {tarea.completada}") 
    assert tarea.completada 
    logger.info("Finalizando test: test_completar_tarea") 
    
def test_listar_tareas(): 
    logger.info("Iniciando test: test_listar_tareas") 
    gestor = GestorTareas() 
    tarea_1 = gestor.agregar_tarea("Estudiar Python") 
    tarea_2 = gestor.agregar_tarea("Escribir cdigo") 
    logger.info("Tareas agregadas:") 
    logger.info(f"Tarea 1: {tarea_1.descripcion}, completada: {tarea_1.completada}") 
    logger.info(f"Tarea 2: {tarea_2.descripcion}, completada: {tarea_2.completada}") 
    gestor.completar_tarea(tarea_1) 
    pendientes = gestor.listar_tareas_pendientes() 
    completadas = gestor.listar_tareas_completadas() 
    logger.info(f"Tareas pendientes: {[t.descripcion for t in pendientes]}") 
    logger.info(f"Tareas completadas: {[t.descripcion for t in completadas]}") 
    assert len(pendientes) == 1 
    assert len(completadas) == 1 
    logger.info("Finalizando test: test_listar_tareas")

