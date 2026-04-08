import simplejson as json
import time
import os

filename = 'myfile.json'

# Verificar si el archivo existe antes de abrirlo
if os.path.exists(filename):
    with open(filename, 'r') as file:
        try:
            variable_json = json.load(file)
            
            # Extraer datos
            token = variable_json.get('token', 'No encontrado')
            expiracion = variable_json.get('expires_at', 0)
            
            # Lógica de tiempo
            tiempo_actual = time.time()
            tiempo_restante = expiracion - tiempo_actual

            print(f"Token: {token}")
            
            if tiempo_restante > 0:
                print(f"El token expira en: {int(tiempo_restante)} segundos")
            else:
                print("¡El token ya ha expirado!")
                
        except json.JSONDecodeError:
            print("Error: El archivo no tiene un formato JSON válido.")
else:
    print(f"Error: El archivo {filename} no existe.")
