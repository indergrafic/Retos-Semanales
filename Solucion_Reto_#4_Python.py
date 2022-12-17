"""/*
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */"""


def areas(base, altura):
    if opcion == 1:
        triangulo = round((base * altura) / 2, 2)
        return triangulo
    elif opcion == 2:
        cuadrado = round(base * altura, 2)
        return cuadrado
    elif opcion == 3:
        restangulo = round(base * altura, 2)
        return restangulo

while True:
    print('''\t.:Menu:.
    1 -> Area del Triángulo.
    2 -> Area del Cuadarado.
    3 -> Area del Rectángulo.
    4 -> Salir''')
    opcion = int(input('\nElige una opción: '))
    if opcion == 4:
        break
    base = float(input('Dime la base en cm.: '))
    altura = float(input('Ahora dime su altura en cm.: '))
    if opcion == 1:
        print(f'El area del triángulo es: ', str(areas(base, altura)))
    elif opcion == 2:
        print('El area del cuadrado es: ', str(areas(base, altura)))
    elif opcion == 3:
        print('El area del restángulo es: ', str(areas(base, altura)))




