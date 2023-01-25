# Creacion
import os.path

archivo = input("Ingrese el nombre de su archivo: ")

if not os.path.exists(archivo):
    print("Creando archivo...")
    f = open(archivo, 'xt')
    f.close()

else:
    f = open(archivo, "wt")
    datos = input("Ingrese los datos a escribir en el archivo: ")
    f.write(datos)
    f.close()