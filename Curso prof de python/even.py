from typing import *

def even_num(number:int) -> str:
    
    list_even=[i for i in range(2,number) if number % i == 0]
    len_list: int = len(list_even) == 1

    if len_list == True:
        return 'El numero SI es primo'
    else:
        return 'El numero NO es primo'

def run():
    ask_num=int(input('Escribe un numero: '))
    print(even_num(ask_num))


if __name__ == '__main__':
    run()
    