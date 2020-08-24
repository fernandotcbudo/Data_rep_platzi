#

def operation(my_dic):

    question_1=str(input('Do you want to change your password? (Y/N): '))

    if question_1 == 'y':
        display=int(input('''
        1. User 1
        2. User 2
        3. User 3
         '''))
    
        if display == 1:
            dis_password_1=str(input('Write new password: '))
            my_dic['UserNumber1'] = (dis_password_1)
            print(f'New password: {my_dic["UserNumber1"][0:]}')

        elif display ==2:
            dis_password_2=str(input('Write new password: '))
            my_dic['UserNumber2'] = (dis_password_2)
            print(f'New password: {my_dic["UserNumber2"][0:]}')

        elif display ==3:
            dis_password_3=str(input('Write new password: '))
            my_dic['UserNumber3'] = (dis_password_3)
            print(f'New password: {my_dic["UserNumber3"][0:]}')

        else:
            print('Write a correct answer')     



    else:
        print('See you later') 
    


def run():
    my_dic={
        'UserNumber1':'1*af',
        'UserNumber2':'2456g',
        'UserNumber3':'5q-gg',
    }

    for password in my_dic.values():
        print(f'Your actual passwords are: {password}')

    operation(my_dic)

    
if __name__ == "__main__":
    print('This is an APP to change passwords')
    run()