import turtle

def main ():
    window=turtle.Screen()
    diego=turtle.Turtle()
    make_square(diego)

    turtle.mainloop()

def make_square(diego):
    lenght=int(input('Tamaño de cuadrado: '))
    for i in range(4):
        make_line(diego,lenght)

def make_line(diego,lenght):
    diego.forward(lenght)
    diego.left(90)

if __name__=='__main__':
    main()








