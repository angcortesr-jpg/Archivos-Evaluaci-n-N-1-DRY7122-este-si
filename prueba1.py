# --- Tarea 1: Información Fija ---
# Reemplaza los nombres con los reales
asignatura = "Evaluación N°1 Programación y Redes Virtualizadas"
nombre = "Angelo Cortés Ramírez"


print("========================================")
print(f"Asignatura: {asignatura}")
print(f"integrantes: {nombre}")
print("========================================\n")

# --- Tarea 2: Solicitar información al usuario ---
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
seccion = input("Introduce tu código de sección: ")
sede = input("Introduce tu sede: ")

print("\n--- Información del Estudiante ---")
print(f"Estudiante: {nombre} {apellido}")
print(f"Sección: {seccion}")
print(f"Sede: {sede}")
print("----------------------------------\n")

# --- Tarea 3: Catalogar ACL ---
try:
    acl = int(input("Introduce el número de ACL IPv4: "))

    if 1 <= acl <= 99:
        print(f"La ACL {acl} es de tipo: ACL Estándar.")
    elif 100 <= acl <= 199:
        print(f"La ACL {acl} es de tipo: ACL Extendida.")
    elif 1300 <= acl <= 1399:
        print(f"La ACL {acl} es de tipo: ACL Estándar (Rango expandido).")
    elif 2000 <= acl <= 2699:
        print(f"La ACL {acl} es de tipo: ACL Extendida (Rango expandido).")
    else:
        print(f"El número {acl} no corresponde a una lista de acceso (ACL) Estándar o Extendida conocida.")

except ValueError:
    print("Error: Por favor, ingresa un número entero válido para la ACL.")
