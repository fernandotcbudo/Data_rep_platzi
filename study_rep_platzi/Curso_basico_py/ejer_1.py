
import random
import sys

sys.setrecursionlimit(10**6)

def operation(b,n):

    if n <= 0:
        return 1
    
    else:
        op1= n * operation(b,(n-2))
        print(op1)
        return op1   
            
    

        
def run():

    b=int(input('Write a number: '))
    n=random.randint(1,10)
    operation(b,n)



if __name__ == "__main__":  
    print('Wellcome to Recursive Algorithim')
    run()
  




