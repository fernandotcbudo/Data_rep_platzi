import random
from os import system

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

#Reads a file with different words
WORD= []
with open("/media/fernandot/FernandoTC/study_rep_platzi/Python_intermedio/files/data.txt","r",encoding="UTF-8") as f:
    for line in f:
      line=line.rstrip()
      WORD.append(line)

#Chooses a random word
def random_words():
      idx= random.randint(0,len(WORD))
      return WORD[idx]
      
#Shows the board
def display_board(hidden_word,tries):
      system('clear')
      print('***************************************')
      print('        The  H A N G  gamE!')
      print('***************************************')
      print(IMAGES[tries]) 
      print('')
      print(hidden_word)
      print('')
      


def run():
      word_r= random_words()
      hidden_word=['_']*len(word_r)
      tries=0

      while True:
            display_board(hidden_word,tries)
            current_word= input('Write a letter: ')
            
            letter_idx=[i for i in range(len(word_r)) if word_r[i] == current_word]

            if len(letter_idx) == 0:
                  tries += 1

                  if tries == 6:
                        display_board(hidden_word,tries)
                        print('')
                        print(f'You lose, the word was {word_r}')
                        break

            else:
                  for i in letter_idx:
                        hidden_word[i]= current_word
                  letter_idx=[]
                  

            try:
                  hidden_word.index('_')

            except ValueError:
                  print('')
                  print(f'You win!!! the word was {word_r}')
                  break

if __name__ == "__main__":     
  run() 