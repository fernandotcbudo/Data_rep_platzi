def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos mexicanos a pesos colombianos')
    print('')

    ammount= float(input('Ingresa la cantidad de pesos mexicanos a convertir:\n'))

    result= foreing_exchange_calculator(ammount)
    print(f'${ammount} pesos mexicanos son {result} pesos colombianos \n')



def foreing_exchange_calculator(ammount):

    mex_to_col_rate= 25.583

    return mex_to_col_rate * ammount



if __name__ == '__main__':
    run()
    print('Final')