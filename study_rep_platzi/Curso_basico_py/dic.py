def run():
    my_dic={
        'Usuario1':'1*af',
        'Usuario2':'2456g',
        'Usuario3':'5q-gg',
    }

    for user,password in my_dic.items():
        print(f'Para el usuario llamado {user} su contraseña es {password}')
        

if __name__ == "__main__":
    run()