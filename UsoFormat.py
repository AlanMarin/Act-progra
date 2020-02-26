# Utiliza la función format de un string, para incrustar valores
# en una salida.

def main():
  Base = 7
  Altura = 5
  AreaTriangulo = (Base * Altura) / 2
  txt = "Area: {2:0} ( {0} por {1} entre dos )"
  print(txt.format (Base, Altura, AreaTriangulo))

#Se empieza de 0 el format