# Creacion
import os.path

if not os.path.exists('archivo.txt'):
    print("Creando archivo...")
    f = open('archivo.txt', 'xt')
    f.close()

else:
    f = open('archivo.txt', "wt")
    datos = input("Ingrese los datos a escribir en el archivo: ")
    f.writelines(datos)
    f.close()