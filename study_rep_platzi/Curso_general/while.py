import random

def run():
    number_found=False
    random_number=random.randint(0,20)
    while not number_found:
        number=float(input('Intenta un numero: '))

        if number == random_number:
            print('Felicidades')

            number_found= True

        elif number > number_found:
            print('El numero es mas pequeño')

        else:
            print('El numero es mas grande')




if __name__ == '__main__':
    run()

