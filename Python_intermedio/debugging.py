
def divisors(num):
    divisors=  [i for i in range(1,num+1) if num % i == 1]
    return divisors


def run():
     num= int(input('Write a number: '))
     print(divisors(num))

if __name__ == '__main__':
    run()
