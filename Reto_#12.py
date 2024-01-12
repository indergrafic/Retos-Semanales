'''
    Crea una funcion que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
    - La funcion recibirá el mes y el año y retornará vedadero o falso.
'''
from datetime import datetime

def friday_13(year: int, month: int) -> bool:
    date = datetime(year, month, 13)
    if date.weekday() == 4:
        return True
    return False
    ''' Resumida la funcion - return datetime(year, month, 13).weekday() == 4 -'''

if __name__ == "__main__":
    print(friday_13(2023, 1))