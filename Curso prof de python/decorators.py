from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron  " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for i in range(1,1000000):
        pass    
@execution_time
def sum(a:int,b:int) -> int:
    return a+b   


if __name__ == '__main__':
    random_func()
    sum(5,6)