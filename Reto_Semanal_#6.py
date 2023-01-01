""" Reto #6
 * INVIRTIENDO CADENAS
 * Fecha publicación enunciado: 07/02/22
 * Fecha publicación resolución: 14/02/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias
 del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
cadena = []
texto = str(input('Dime una palabra o frase: '))

for i in texto:
    cadena.insert(0, i)

for i in cadena[:]:
    print(f'{i}', end='')



