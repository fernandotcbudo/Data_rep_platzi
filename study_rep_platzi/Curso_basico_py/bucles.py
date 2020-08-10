def run():
    LIMIT=1000
    counter=0
    base=2**counter

    while base < LIMIT:
        print(base)
        counter= counter + 1
        base= 2**counter

    return 'Finalizado'

if __name__ == "__main__":
    final=run()
    print(final)