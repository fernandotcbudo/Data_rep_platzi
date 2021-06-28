#Example of Exhaustive enumeration

def calcul_root(root,number):
    while root**2 < number:
        root += 1
    if root**2==number:
        print(f'The square root of {number} is {root}')
    else:
        print(f'The square root of {number} is not a whole number ')



if __name__ == '__main__':
    number=int(input('Write a number: '))
    root=0
    calcul_root(root,number)
