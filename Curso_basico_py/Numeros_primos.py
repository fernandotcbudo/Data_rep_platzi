def es_primo(num):
    counter=0

    for i in range(1,num+1):
        if i == 1 or i == num:
            continue
        elif num % i == 0:
            counter += 1

    if counter == 0:
        return True 
    else:
        return False 


def run():
    num=int(input('Digita un numero: '))
    if es_primo(num):
        print('Es primo')

    else:
        print('No es primo')



if __name__ == "__main__":
    run()