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

NUM= []
with open("/media/fernandot/FernandoTC/study_rep_platzi/Python_intermedio/files/data.txt","r",encoding="UTF-8") as f:
    for line in f:
        NUM.append(line)
    print(NUM)






def run():
      pass

if __name__ == "__main__":
  print('***************************************')
  print(' The  H A N G - GAME!')
  print('***************************************')
  run()