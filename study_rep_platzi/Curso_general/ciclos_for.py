def my_square(sample):
    list=[]

    for i in sample:

        list.append(i**2)

    return list


if __name__ == '__main__':
    print(my_square([1, 2, 3, 4, 5, 6, 7, 8, 9]))



