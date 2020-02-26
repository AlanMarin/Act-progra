
variableglobal="Soy global"


def pendiente():
    pass

def norecibeargumentos():

    variableglobal=4
    print("No recibe argumentos")
    print(variableglobal)

# Los argumentos se dentro de parentesis en forma
# de lista separada por comas.
def recibeargumentos(fname, lname):
    print(fname + " " + lname)
    print(variableglobal)

# Un argumento es opcional cuando le asignas un valor 
# al momento de su declaracion.
# Los argumentos opcionales siempre van al final de la 
# lista de argumentos.
def argumentosopcionales(city, country = "Mexico"):
    print("Soy de " + city + ", " + country)

# Si se especifica return, la funcion retorna valores 
# Cuidar que el flujo del programa siempre los retorne
# Se debe utilizar como expresion, atendiendo el 
# retorno correspondiente
def elevoalcuadrado(x):
  return x * x

def main():
    # norecibeargumentos()
    # recibeargumentos("Alan", "Marin")
    # argumentosopcionales("Monterrey")
    # argumentosopcionales("Barcelona", "España")
    print(elevoalcuadrado(4))
