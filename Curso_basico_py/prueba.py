from math import sin, cos, exp, log

def operation(inpunt_1,inpunt_2):

    if inpunt_1 == 1:
        seno= sin(inpunt_2)
        print(seno)
    elif inpunt_1 == 2:
        conseno= cos(inpunt_2)
        print(conseno)
    elif inpunt_1 == 3:
        expo= exp(inpunt_2)
        print(expo)
    elif inpunt_1 == 4:
        logarit= log(inpunt_2)
        print(logarit)
    else:
        print('Introduce un valor valido')

    

         

def run():
    inpunt_1=int(input('Introduce la funcion a aplicar: '))
    inpunt_2=int(input('Introduce un entero positivo: '))
    operation(inpunt_1,inpunt_2)


if __name__ == "__main__":
    run()