def run():
    counter=0
    with open ('lluvia.txt', encoding="utf8") as f_i:
        for line in f_i:
            counter += line.count('lluvia')

    print(f'Lluvia se encuentra {counter} veces en el texto')


if __name__ == '__main__':
    run()
