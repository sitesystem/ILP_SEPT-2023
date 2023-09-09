# Ejemplo 2. Operaciones Matemáticas
# Importar librerías o bibliotecas con funciones matemáticas
import math

# ENTRADA DE DATOS
# Declarar o crear variables
número_1 = float(input("Escribe un número: "))
número_2 = float(input('Escribe otro número: '))
# Declar o crear constantes
PI = 3.1416

# PROCESOS (Cálculos u Operaciones Matemáticas y/o Lógicas)
suma = número_1 + número_2
resta = número_1 - número_2
multiplación = número_1 * número_2
división = número_1 / número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

múdulo_residuo = número_1 % número_2 

# SALIDA DE DATOS
# Imprimir o mostrar resultados en pantalla
print("Suma =", round(suma, 2))
print("Resta =", round(resta, 2))
print("Multiplación =", round(multiplación, 2))
print("División =", división)
print("Módulo/Residuo =", múdulo_residuo)
