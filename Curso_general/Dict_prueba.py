calificaciones = {}
calificaciones['Algoritmos'] = '9'
calificaciones['Matematicas'] = '10'
calificaciones['Ciencia de datos'] = '8'
calificaciones['Bases de datos'] = '10'


def main():
    for key, values in calificaciones.items():
        print(f'Tu nota en {key} fue: {values}')


def promedio():
    suma_calif= 0
    for calificacion in calificaciones.values():
        suma_calif += int(calificacion)

    suma_calif2=suma_calif//len(calificaciones.values())

    print(f'El promedio de calificaciones es {suma_calif2}')

if __name__ == '__main__':
    main()
    promedio()



