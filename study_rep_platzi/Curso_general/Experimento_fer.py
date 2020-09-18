import random

def listaAleatorios(n):
    lista = []
    for i in range(n):
        lista.insert(i, random.randrange(0, 100))


    lista_2 = []

    for i in lista:
        lista_2.insert(i,i**2)


    print(f'Los numeros aleatorios son {lista} y sus exponentes son {lista_2}')

if __name__ == '__main__':
    print("Ingrese cuantos numeros aleatorios desea obtener")
    n = int(input())
    aleatorios=listaAleatorios(n)

