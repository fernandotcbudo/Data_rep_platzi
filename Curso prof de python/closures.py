# Ejemplo de programacion con closures - Funcion que repite un string el numero de veces que le indiquemos

#def main_rep(n):
    #def repeater(string):
        #assert type(string) == str,"Solo puedes agregar palabras"
        #return string * n
    #return repeater

#def run():
    #rep5= main_rep(5)
    #print(rep5("Diego "))
    #rep9= main_rep(9)
    #print(rep9("Paula "))
    
#if __name__=='__main__':
    #run()
    
# Ejemplo dos

def make_div(n:int):
    def div(x:int):
        assert type(n) == int, "Solo funciona con numeros"
        return x//n
    return div

def run():

    div_by_3=make_div(3)
    print(div_by_3(18))
    
if __name__ == '__main__':
    run()    
