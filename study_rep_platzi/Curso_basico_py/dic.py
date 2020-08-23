#

def operation(my_dic):

    question_1=str(input('Do you want to change your password? (Y/N): '))

    if question_1 == 'Y' or 'y':

        display=int(input('''
        1. User 1
        2. User 2
        3. User 3

        ''')
        
    
        if display == 1:
            new_1=str(input('Write password for User 1: '))
            my_dic.update(new_1)

    

        


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
    run()