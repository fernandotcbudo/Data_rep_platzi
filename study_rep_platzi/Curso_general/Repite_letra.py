"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""


def first_not(char_seq):
    seen_letters={}

    for idx,letter in enumerate(char_seq):
        if letter not in seen_letters:
            seen_letters[letter]=(idx,1)
        else:
            seen_letters[letter] = (seen_letters[letter][0],seen_letters[letter][1] + 1)

    final_letters= []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key,value[0]))

    not_rep_let= sorted(final_letters,key=lambda value: value[1])

    if not_rep_let:
        return not_rep_let[0] [0]

    else:
        return '_'

if __name__ == '__main__':
    char_seq=str(input('Escribe una secuencia de caracteres: '))
    result=first_not(char_seq)

    if result == '_':
        print('Todos los caracteres se repiten')

    else:
        print(f'El primer caracter no repetido es {result}')