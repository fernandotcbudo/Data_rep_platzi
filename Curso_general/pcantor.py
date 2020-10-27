#FUNCTIONS
def x(param1,param2,**others):
    for i in others.items():
        print(i)

if __name__ == "__main__":
    x(1,2,tercero=3)

def multip(y,z):
    y= y+3
    z.append(23)
    print(y,z)

if __name__ == "__main__":
    y=22
    z=[22]
    multip(y,z)
    print(y,z)
    

def sum(num1,num2):
    return num1 + num2
    

if __name__ == "__main__":
    print(sum(1,2))

