import random


def run():
    al_num=random.randint(1,100)
    ch_mun=int(input('Elige un numero de 1 a 100\n'))

    while ch_mun != al_num:
        if ch_mun < al_num:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas pequeño')
        ch_mun=int(input('Elige otro numero: '))


    print('¡Ganaste!')



if __name__ == "__main__":
    run()