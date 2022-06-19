# Importamos librerias
import funcion
# Pedimos datos
ruta = funcion.compro("Ingrese la ruta de su archivo.py: ")

# Contamos las lineas de codigo
arch = open(ruta,"r", encoding="utf-8")
num = len (arch.readlines())
print(num)

arch.close