from typing import *

def is_palindrome(word: str) -> bool:
    word = word.replace(" ","").lower()
    return word == word[::-1]

def run():
    print(is_palindrome(1000))
    
if __name__ =="__main__":
    run()