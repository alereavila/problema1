"""""
Problema : Objetivo: Conversion de temperatura
Usuario: General
SO: Windows, Linux, MAC
Interface: Cline
Autor: alereavila (alereavila8@gmail.com)

"""
print("CONVERSION DE TEMPERATURA")
cantidad=float(input("Introduce la cantidad que quieres convertir:  "))
centigrados = cantidad-273.15
print("En grados Centigras es ", centigrados)
fahrenheit= (9/5)* centigrados+32
print("En grados Fahrenheit es ", fahrenheit)