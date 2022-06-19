# Importamos librerias
import re
texto = ("@robot9! @robot4& I have a good feeling that the show is going to be amazing! @robot9$@robot7%")

cadena = re.findall(r"@robot\d\D", texto)

print(cadena)