from pyfiglet import Figlet
figlet = Figlet()

figlet.getFonts()
fuente = input("Ingrese la fuente: ")

figlet.setFont(font=fuente)

nombre = input("Ingrese una palabra: ")

print(figlet.renderText(nombre))