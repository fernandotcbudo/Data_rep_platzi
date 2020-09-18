#suma recursiva

def recursive_numb(number):
    if number != 0:
        return number + recursive_numb(number - 1)
    else:
        return number



def run():

    is_not_number= True
    while True:
        number=int(input('Por favor ingresa un numero entero: '))
        if number < 1:
            print('Por favor ingresa un numero mayor que 1')

        final_result= recursive_numb(number)

        print(f'El resultado es {final_result}')
        break


if __name__=='__main__':
    run()