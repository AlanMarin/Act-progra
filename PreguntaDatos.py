# Pregunta diferentes tipos de datos, sin validación.

# Importa el módulo requerido para usar datos de tipo Date.
import datetime

def main():
 # Los datos string se preguntan y procesan sin intermediación.
 strDato = input("Dame un dato string: ")
 # Los datos numéricos se preguntan por intermediación.
 _iDato = input("Dame un dato entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato float: ")
 fDato =float(_fDato)
 # Los datos date se preguntan por intermediación.
 _dtDato = input("Dame una fecha yyyy/mm/dd: ")
 #sustrae la posicion empezando por 0
 anio=_dtDato[0:4]
 mes=_dtDato[5:7]
 dia=_dtDato[-2:]
 print(anio)
 print(mes)
 print(dia)

 dtDato = datetime.datetime(int(anio), int(mes), int(dia))

 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))