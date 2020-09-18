import random

def password_generator():
    list_1= ['A','B','C','D','E','F','G']
    list_2= ['a','b','c','d','e','f','g']
    list_3= ['!','*','$','?','%','#']
    list_4= ['1','2','3','4','5','6','7']
    charac= list_1+list_2+list_3+list_4

    aleat= []

    for i in range(10):
        random_char= random.choice(charac)
        aleat.append(random_char)

    aleat= ''.join(aleat)
    return aleat



def run():
    password= password_generator()
    print('BIENVENIDO A TU GENERADOR DE CONTRASEÑAS')
    print(f'Tu nueva contraseña es {password}')




if __name__ == "__main__":
    run()