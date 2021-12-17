def palind(word):
    word= word.replace(' ','')
    word= word.lower()
    inverted_word=word[:: -1]
    if word == inverted_word:
        return True
    else:
        return False


def run():
    word=str(input('Escribe una palabra: '))
    is_palin= palind(word)
    if is_palin == True:
        print('Es palindromo')

    else:
        print('No es palindromo')



if __name__ == "__main__":
    run()