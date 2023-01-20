"""
*
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.


Programa resumido para no teclear todo el código Morse
"""

morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "..", "e": "."}

palabra = input('Escribe una palabra: ')

for i in palabra:
    if i == " ":
        print("/*/ ", end="")
    else:
        print(morse[i], " ", end="")
