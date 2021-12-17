
def main():
    to_find_num= int(input('Write a number: '))
    epsilon=0.01
    pass_2=epsilon**2
    answer=0.0
    while abs(answer**2 - to_find_num) >= epsilon and answer <= to_find_num:
        answer += pass_2

    if abs(answer**2 - to_find_num) >= epsilon:
        print(f'Square root of {to_find_num} does not exists')
    else:
        print(f'Square root of {to_find_num} is {answer}')
 

if __name__ == '__main__':
    main()