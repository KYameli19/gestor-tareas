# gestor_tareas.py

tareas = []

def mostrar_menu():
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar_tarea():
    tarea = input("Ingrese una nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")

def listar_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def eliminar_tarea():
    listar_tareas()
    try:
        indice = int(input("Número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            eliminada = tareas.pop(indice)
            print(f"Tarea '{eliminada}' eliminada.")
        else:
            print("Índice no válido.")
    except ValueError:
        print("Entrada inválida.")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
