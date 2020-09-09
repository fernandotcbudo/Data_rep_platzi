#Exercise to practice getters and setters
#Exercise to practice arrays
class Product():

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

class Order():

    def __init__(self,products,amounts):
        self.__products=products
        self.__amounts=amounts  

    def total_order(self):

        total=0

        for (p,a) in zip(self.__products,self.__amounts):
            total= total + p.cal_total(a)

        return total

       
    def show_order(self):
        for (p,a) in zip(self.__products,self.__amounts):
            print(f'Product: {p.name} Amount: {a}')


p1=Product(1,'Banana',12)
p2=Product(2,'Apple',20)
p3=Product(3,'Orange',18)

list_prod=[p1,p2,p3]
new_amounts=[5,10,20]
new_order=Order(list_prod,new_amounts)

if __name__ == "__main__":
    print('Wellcome to PRICE MARKET!')
    print(f'{p1} total cost is of this product: {p1.cal_total(5)}')
    print('Now you can order more!')
    print(f'Total order: {new_order.total_order()} ')
    new_order.show_order()




    
