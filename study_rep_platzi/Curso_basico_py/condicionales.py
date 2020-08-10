
def edades(edad):
    
    if edad > 18:
        print('Eres mayor de edad')

    else:
        print('Eres menor de edad')
        
if __name__ == "__main__":
    edad=int(input('Escribe tu edad: '))
    edades(edad)

