# Funcion

def nivel (msg: str = "Ingrese un valor adecuado para el nivel: "):
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except:
        return nivel(msg)
