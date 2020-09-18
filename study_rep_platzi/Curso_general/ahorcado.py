import random

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS= [
    'lavadora',
    'jiujitsu,',
    'computadora',
    'quimica',
    'inteligencia',
    'artificial',
    'grafeno',
    'boxeo',
    ]

def show_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('_____*_____*_____*_____*_____*_____*_____*')


def random_word():
    idx= random.randint(0,len(WORDS)-1)
    return WORDS [idx]

def run():
    word=random_word()
    hidden_word=['-'] * len(word)
    tries= 0

    while True:
        show_board(hidden_word,tries)
        current_letter=str(input('Escoje una letra: '))

        letter_idx= []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_idx.append(i)

        if len(letter_idx) == 0:
            tries += 1

            if tries == 6:
                show_board(hidden_word,tries)
                print('')
                print(f'¡PERDISTE! La palabra correcta era {word}')
                break

        else:
            for i in letter_idx:
                hidden_word[i]= current_letter

            letter_idx= []

        try:
            hidden_word.index('-')

        except ValueError:
            print(f'¡MUY BIEN!Ganaste la palabra es {word} ')
            break



if __name__ == '__main__':
    print('***************************************')
    print(' ¡J U E G O   D E L   A H O R C A D O!')
    print('***************************************')
    run()