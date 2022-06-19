# Funcion
def flo (msg: str = "Es un valor decimal: "):
    """Solicita un número entero"""
    try:
        x = float(input(msg))
        return x
    except:
        return flo(msg)