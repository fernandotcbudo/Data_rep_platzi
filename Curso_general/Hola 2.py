nombre1=input('Cual es tu nombre: ')
print(f'Hola {nombre1} vamos a calcular la raiz cuadrada de un numero')

objetivo=float(input('Digita un numero: '))

#Enumeracion
def enumeracion():
    respuesta=0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f' La raiz del {objetivo} es la {respuesta}')
    else:
        print(f'El numero {objetivo} no tiene una raiz cuadrada exacta')

#Aproximacion
def aproximacion():
    epsilon=0.01
    paso=epsilon**2
    respuesta=0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2-objetivo), respuesta)

    if abs (respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

#Binaria
def binaria():
    epsilon=0.01
    bajo=0.0
    alto=max(1.0,objetivo)
    respuesta= (alto+bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo},alto={alto},respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo=respuesta
        else:
            alto=respuesta
        respuesta = (alto+bajo)/2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

print('Con estos metodos puedes calcularla')
print('1. Enumeracion')
print('2. Aproximacion')
print('3. Binaria')
metodo=int(input('Escoje un metodo'))

if metodo == 1:
    enumeracion()
elif metodo == 2:
    aproximacion()
elif metodo == 3:
    binaria()
else:
    print('Ninguno de estos metodos esta definido')
