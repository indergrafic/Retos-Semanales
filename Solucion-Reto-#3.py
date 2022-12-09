'''/*
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.'''

# Se nos pide ingresar un numero.

primos = []
i = 2
n = 2
for i in range(100):
    if n == i:
        continue
    if n%i == 0:
        primos.append(n)
    n +=1

num = int(input(f'Qué número quieres saber si es primo : '))
for i in primos:
    if i == num:
        print(f'El {num} es un numero primo')
    else:
        print(f'El {num} indicado no es un primo')
print(f'''Estos son los primos entre los 100 primeros números:/
      {primos[:]}''')
