#This program returns the standard deviation of a range of numbers
import statistics

def exp(num):
    print(f'This program will show you the standard deviation of the list of numbers that you picked')
    stat= statistics.pstdev(num)
    print(round(stat,2))
    


def run():
    display='''
    PICK A LIST OF NUMBERS
    1. List 1 to 20
    2. List 21 to 30
    3. List 31 to 40
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