countries= {
    'colombia':'48 millones',
    'mexico':'122 millones',
    'venezuela':'49 millones',
    'argentina':'40 millones',
    'peru':'39 millones',
    'chile':'18 millones',
}

while True:
    country=str(input('Nombre de un pais: ')).lower()
    try:
        print(f'La poblacion de {country} es {countries[country]}')

    except KeyError:
        print(f'No tenemos la poblacion de {country}')





