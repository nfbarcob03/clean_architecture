import pytest 
import logging 
from pytest_bdd import scenarios, given, when, then 
from app.gestor_tareas import GestorTareas 
# Configurar el logger 

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__) 
#Cargar los escenarios desde el archivo .feature 
scenarios('features/gestor_tareas.feature') 

# Fixtures 
@pytest.fixture 
def gestor(): 
    logger.info("Inicializando GestorTareas fixture") 
    return GestorTareas() 

# Given Steps 
@given('que el gestor de tareas está vacío')
def gestor_vacio(gestor): 
    logger.info("Verificando que el gestor de tareas est vaco") 
    assert len(gestor.tareas) == 0 
    
@given('que el gestor de tareas tiene una tarea "Estudiar Python"') 
def gestor_con_tarea(gestor): 
    logger.info('Agregando tarea "Estudiar Python" al gestor de tareas') 
    gestor.agregar_tarea("Estudiar Python") 
    
# When Steps 

@when('agrego una tarea "Estudiar Python"') 
def agregar_tarea(gestor):
    logger.info('Agregando tarea "Estudiar Python" al gestor de tareas') 
    gestor.agregar_tarea("Estudiar Python") 
    
@when('marco la tarea "Estudiar Python" como completada') 
def completar_tarea(gestor): 
    logger.info('Marcando tarea "Estudiar Python" como completada') 
    tarea = next(t for t in gestor.listar_tareas_pendientes() if t.descripcion == "Estudiar Python") 
    gestor.completar_tarea(tarea) 
    # Then Steps
    # 
@then('la lista de tareas pendientes debe contener "Estudiar Python"') 
def verificar_tarea_pendiente(gestor): 
    tareas_pendientes = [t.descripcion for t in gestor.listar_tareas_pendientes()] 
    logger.info(f"Tareas pendientes actuales: {tareas_pendientes}") 
    assert "Estudiar Python" in tareas_pendientes, f"Tareas pendientes: {tareas_pendientes}" 
    
@then('la lista de tareas completadas debe contener "Estudiar Python"') 
def verificar_tarea_completada(gestor): 
    tareas_completadas = [t.descripcion for t in gestor.listar_tareas_completadas()] 
    logger.info(f"Tareas completadas actuales: {tareas_completadas}") 
    assert "Estudiar Python" in tareas_completadas, f"Tareas completadas: {tareas_completadas}"