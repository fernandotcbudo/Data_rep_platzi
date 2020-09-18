def lista_temp(temp):
    sum_of_temps=0
    for temp in temps:
            sum_of_temps += temp

    return sum_of_temps / len(temps)


if __name__ =='__main__':
    temps=[21,24,23,22,25,20,24]
    average=lista_temp(temps)
    print(f'La temperatura promedio es {average}')