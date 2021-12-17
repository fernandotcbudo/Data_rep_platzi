from Poo_2_mod import Grappler
def run():
    grappler_1 = Grappler(is_get_up=False)

    while True:
        command=str(input('''
        ¿Que deseas hacer?
        [L]evantar al luchador
        [D]erribar al luchador 
        [S]alir
        '''))

        if command == 'l':
            grappler_1.get_up()

        elif command == 'd':
            grappler_1.take_down()

        else:
            break


if __name__ == '__main__':
    run()