# Pregunta un dato hasta que sea correcto
# Importa el módulo requerido para usar Regular Expressions.
import re

def main():
  while True:
    strRFC = input("Dame el RFC: ")
    coincide = re.search("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)
    if (coincide):
      print("RFC Correcto!")
      break
    else:
      print("RFC incorrecto. Intenta de nuevo.")
#Se corta hsta que el dato sea valido o correcto