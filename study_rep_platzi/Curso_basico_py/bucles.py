#This function returns, the exponential of a random number which its base is a number from 1 to 9999.
import random
def run():
    LIMIT=10000
    counter=0
    aleatory_num=random.randint(2,10)
    base=counter**aleatory_num
    
    while base < LIMIT:
        print(base)
        counter= counter + 1
        base= counter**aleatory_num
    print(f'The last random expo was {aleatory_num}')


if __name__ == "__main__":
    print('Wellcome to Random Expo!')
    run()