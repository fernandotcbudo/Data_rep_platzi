def binari_search(numbers,number_find,low,high):
    if low > high:
        return False

    mid=(low+high)//2

    if numbers[mid] == number_find:
        return True
    elif numbers[mid] > number_find:
        return binari_search(numbers,number_find, low, mid-1)
    else:
        return binari_search(numbers,number_find,mid+1,high)

if __name__ == '__main__':
    numbers=[1,2,3,4,6,8,9,11,12,14,20,25,30]
    number_find=int(input('Ingresa un numero: '))
    result=binari_search(numbers,number_find,0,len(numbers)-1)
    if result is True:
        print('Numero si esta en la lista')

    else:
        print('Numero no esta en la lista')
