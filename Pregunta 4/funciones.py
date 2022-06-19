# Funcion
def flo (msg: str = "Es un valor entero "):
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except:
        return flo(msg)