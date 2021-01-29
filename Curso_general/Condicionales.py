def saludo():
    gender_user=str(input('¿Eres hombre o mujer?\n'))
    if gender_user == 'Hombre':
        print('Buenos dias señor')
    elif gender_user =='hombre':

        print('Buenos dias señor')

    else:
        print('Buenos dias señorita')

if __name__ == '__main__':
    saludo()


