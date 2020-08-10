#Funcion 1
def palindrome2(word):
    reverse_word= word[::-1]

    if reverse_word == word:
        return True
    else:
        return False
#Funcion 2
def palindrome(word):

    reverse_letter=[]

    for i in word:
        reverse_letter.insert(0,i)

    reverse_word=''.join(reverse_letter)

    if reverse_word == word:
        return True
    else:
        return False


if __name__ == '__main__':
    word=str(input('Escribe una palabra: '))
    result=palindrome2(word)
    if result == True:
        print(f'{word} si es un palindromo')
    else:
        print(f'{word} no es un palindromo')



