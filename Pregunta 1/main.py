# Importamos librerias
import funciones as fun
import random
# Constantes
MSG = "Bienvenido al juego ADIVINA EL NÚMERO "
# Funciones
def main():
    print(MSG)
    control = 0
    entrada = fun.nivel("Ingrese el nivel del juego: ") 

    while (control < 6):
        numeromin = 1
        numeromax = entrada
        adivina = random.randint(numeromin, numeromax)
        adiv = int(input("ADIVINA EL NÚMERO: "))

        if (adiv == adivina):
            print("¡¡¡¡¡Adivinaste el Número!!!!! ")
            print("GANASTE ")
            break
        elif (adiv > adivina):
            print("¡Te pasaste! ")  
        elif (adiv < adivina):
            print("¡Demasiado pequeño!")     
        else:
            print("Número de intentos superados ¡PERDISTE! ")
            print(control)
        control = control + 1

# Mi programa
main()