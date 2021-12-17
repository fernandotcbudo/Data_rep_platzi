
def divisors(num):
    divisors=  [i for i in range(1,num+1) if num % i == 0]
    return divisors


def run():
    try:
        num= (int(input('Write a number: ')))
        assert num >= 0, 'Negative number'
        print(divisors(num))
    except ValueError:
        print('Please write a number')


if __name__ == '__main__':
    run()
