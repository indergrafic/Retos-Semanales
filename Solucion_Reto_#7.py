"""
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de
 todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente."""


frase = str(input('Escribe una frase:'))
frase = frase.lower()
frase_sep = frase.split()

espacios = 0

print(f'\nLa Frase tiene: ', len(frase_sep), 'palabras.')
print(frase_sep)
print(frase)

veces = 0
i = 0
for i in range(len(frase_sep)):
	if frase_sep[i] in frase:
		veces += 1

	print(f'\n La palabra: {frase_sep[i]} se repite {veces} vez')
	
	