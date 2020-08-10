def exp(num):
    print(f'Este programa devuelve el exponente cuadrado, de cada numero de la lista que eligiste')
    for n in num:
        print(n**2)


def run():
    display='''
    SELECIONA UNA LISTA DE NUMEROS
    1. Lista del 1 al 20
    2. Lista del 21 al 30
    3. Lista del 31 al 40
    '''
    option=int(input(display))

    if option == 1:
        exp(list(range(1,21)))

    elif option ==2:
        exp(list(range(21,31)))

    elif option ==3:
        exp(list(range(31,41)))

    else:
        print('Ingresa una opcion valida')


if __name__ == "__main__":
    run()