Feature: Gestión de Tareas
  Como usuario quiero gestionar mis tareas para poder mantenerme organizado.

  Scenario: Agregar una tarea
    Given que el gestor de tareas está vacío
    When agrego una tarea "Estudiar Python"
    Then la lista de tareas pendientes debe contener "Estudiar Python"

  Scenario: Completar una tarea
    Given que el gestor de tareas tiene una tarea "Estudiar Python"
    When marco la tarea "Estudiar Python" como completada
    Then la lista de tareas completadas debe contener "Estudiar Python"