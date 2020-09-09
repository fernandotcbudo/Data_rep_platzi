#Exercise to practice getters and setters

class product():

    def __init__ (self,code,name,price):
        self.__code=code
        self.__name=name
        self.__price=price


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self,value):
        self.__code=value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name=value


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        self.__price=value

    def cal_total(self,units):
        return self.price * units

    def __str__(self):
        return 'Code: ' + str(self.__code ) + ', Name: ' + str(self.__name ) + ', Price: ' + str(self.__price)

p1=product(1,'Banana',12)
p2=product(2,'Apple',20)
p3=product(3,'Orange',18)


if __name__ == "__main__":
    print(f'{p1} your total cost is: {p1.cal_total(5)}')

    
