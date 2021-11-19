from src.util import replaceSpaceByGuion
from src.util import mayusculasPorMinusculas
from src.util import sustituyeIndiceConLetra
from src.util import capitalizacion

#Inicializo variables
string = input("Ingrese una frase: ")
indice = 100
letra = 0

#Compruebo que el indice sea menor que el tamaño de la cadena
while indice>len(string):
    indice = (input("Ingrese un numero para el indice a remplazar: "))

letra = input("Ingrese una letra para sustituir: ")

#Probando ejercicio 1
cadenaNueva1 = replaceSpaceByGuion(string)
print(cadenaNueva1)

#Probando ejercicio 2
cadenaNueva2 = mayusculasPorMinusculas(string)
print(cadenaNueva2)

#Probando ejercicio 3
cadenaNueva3 = sustituyeIndiceConLetra(string, indice, letra)
print(cadenaNueva3)

#Probando ejercicio 4
cadenaNueva4 = capitalizacion(string)
print(cadenaNueva4)