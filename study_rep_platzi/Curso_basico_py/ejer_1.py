
def run():
    pesos=int(input('''
    
    Bienvenido a tu conversor de moneda:

    Elige tu moneda

    1. Pesos colombianos 
    2. Pesos argentinos 
    3. Pesos mexicanos 
      ''')) 
    
    numero_pesos=int(input('''
    Digita cuantos pesos tienes: 
    '''))
    
    if pesos == 1:
        print(f'Tus pesos colombianos equivalen a {round(numero_pesos/3875,1)} dolares')
     
    elif pesos == 2:
        print(f'Tus pesos argentinos equivalen a {round(numero_pesos/65,1)} dolares')
         
    elif pesos ==3:
        print(f'Tus pesos mexicanos equivalen a {round(numero_pesos/24,1)} dolares')  
    else:
        print('Ingresa una opcion valida')
     
if __name__ == "__main__":  
    run()



