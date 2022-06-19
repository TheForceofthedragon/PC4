# Importamos librerias
import funciones

n = int(input("Ingresa un número del 1 al 10: "))
lista = []

for i in range(1, 13):
    Texto = f"{n} x {i} = {n*i}\n"
    lista.append(Texto)

open(f'tabla-{n}.txt', 'w').writelines(lista)
