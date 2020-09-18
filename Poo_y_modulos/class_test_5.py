#Exercise to practice getters and setters
#Exercise to practice arrays
#Exercise to practice try and except 

TYPE_DIS_F='Fixed'
TYPE_DIS_P='Percentage'


class Discount():

    def __init__(self,type,value):
        
        if not isinstance(value,int):
            raise ValueError('Value must be a number')
        if not isinstance(type,str):
            raise ValueError('Type must be a string')
        if type != TYPE_DIS_P and type != TYPE_DIS_F:
            raise ValueError('Please check')
        if type == TYPE_DIS_F and value <= 0:
            raise ValueError('Fixed type must be greater than zero')
        if type == TYPE_DIS_P and (value<=0 or value>100):
            raise ValueError('Percentage type must be between 1 and 100')

        self.__type= type
        self.__value= value    

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self,type):
        self.__type= value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,value):
        self.__value=value

    def apply_discount(self,price):

        if self.__type == TYPE_DIS_F:
            if price > self.__value:
                return price - self.__value

            else:
                return 0

        else: 
            return price - (price * (self.__value/100))


class Product():

    def __init__ (self,code,name,price,discount= None):
        self.__code=code
        self.__name=name
        self.__price=price
        self.__discount=discount


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
        if self.__discount == None:
            return self.__price

        else:
            return self.__discount.apply_discount(self.__price)

    @price.setter
    def price(self,value):
        self.__price=value

    def cal_total(self,units):
        return self.price * units

    def __str__(self):
        return 'Code: ' + str(self.__code ) + ', Name: ' + str(self.__name ) + ', Price: ' + str(self.__price)

class Order():

    def __init__(self):
        self.__products=[]
        self.__amounts=[]  
#This function adds a product 
    def add_pro (self,product,amount):
        
        if not isinstance(product,Product):
            raise Exception('Product must be correct')

        if not isinstance(amount,int):
            raise Exception('Amount must be a number')

        if amount <= 0:
            raise Exception('Amount must be greater than zero')

        if product in self.__products:
            index= self.__products.index(product)
            self.__amounts[index] = self.__amounts[index] + amount
        else:
            self.__products.append(product)
            self.__amounts.append(amount)

#This function removes a product 
    def remove_pro (self,product):  
        if not isinstance(product,Product):
            raise Exception('Product must be correct')

        if product in self.__products:
            index= self.__products.index(product)
            del self.__products[index]
            del self.__amounts[index]

        else:
            raise Exception('The product does not exists')


#This shows the sum of the cost of an order 
    def total_order(self):

        total=0

        for (p,a) in zip(self.__products,self.__amounts):
            total= total + p.cal_total(a)

        return total

 #This shows the total order       
    def show_order(self):
        for (p,a) in zip(self.__products,self.__amounts):
            print(f'Product: {p.name} Amount: {a}')


d1=Discount(TYPE_DIS_F,12)
d2=Discount(TYPE_DIS_P,50)
d3=Discount(TYPE_DIS_F,10)

p1=Product(1,'Banana',12,d3)
p2=Product(2,'Apple',20,d1)
p3=Product(3,'Orange',18,d2)

new_order=Order()


if __name__ == "__main__":
    print('Wellcome to PRICE MARKET!')
    try:
        new_order.add_pro(p1,10)
        new_order.add_pro(p2,5)
        new_order.add_pro(p3,5)

        print(f'total cost is of this order: {new_order.total_order()}')

        new_order.show_order()

        new_order.remove_pro(p1)

        print(f'total cost is of this order: {new_order.total_order()}')

        new_order.show_order()




    except Exception as e:
        print(e)









    
