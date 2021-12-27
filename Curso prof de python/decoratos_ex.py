def my_decorator(func):
    def wrapper(*args,**kwargs):
        num= func(*args,**kwargs)
        prom=num//2
        print('El promedio es: ' + str(prom))
    return wrapper
    
@my_decorator
def add(a:int,b:int) -> int:
    return a + b

if __name__ == '__main__':
    a=int(input("Ingresa el primer numero: "))
    b=int(input("Ingresa el segundo numero: "))
    add(a,b)