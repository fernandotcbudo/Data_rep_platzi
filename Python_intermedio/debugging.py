def divisors(num):
    try:
        if num == 0:
            raise ValueError('Empty string')
        divisors=  [i for i in range(1,num+1) if num % i == 0]
        return divisors

    except ValueError as ve:
        print(ve)
        return False 


def run():
    try:
     num= int(input('Write a number: '))
     print(divisors(num))
     print('Program is over')
    except ValueError:
     print('Please write a number')   

if __name__ == '__main__':
    run()
