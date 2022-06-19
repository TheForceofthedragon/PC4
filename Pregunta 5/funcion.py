# Funcion
def compro (msg: str = "Es una ruta "):
    """Solicita un string"""
    try:
        x = str(input(msg))
        return x
    except:
        return compro(msg)