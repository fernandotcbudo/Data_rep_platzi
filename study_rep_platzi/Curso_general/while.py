#In this game you have to guess random 3 numbers 

import random

def run():
    number_found=False
    random_list=range(1,10)
    sample_list= random.sample(random_list,k=3)
    print(sample_list)


    while not number_found:
        number_list=[]
    
        number_1=int(input('Intenta un numero: '))
        number_list.append(number_1)
        number_2=int(input('Intenta un numero: '))
        number_list.append(number_2)
        number_3=int(input('Intenta un numero: '))
        number_list.append(number_3)
        print(number_list)

        if number_list == sample_list:
            print('Felicidades')

            number_found= True

        else:
            print('Try again with other tree numbers')




if __name__ == '__main__':
    print('Welcome to: guess a number!')
    run()

