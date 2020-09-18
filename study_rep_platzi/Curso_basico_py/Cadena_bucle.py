
def run():
    num=str(input('Escribe una frase: '))
    counter=len(num)
    LIMIT=8
  
    while counter < LIMIT:
        for let in num:
            print(let)
            counter += 1    
        break 

if __name__ == "__main__":
    run()   