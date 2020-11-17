#POO CLASES OBJECTS - HERITAGE - ENCAPSULATION
class Robot:
    """Class constructor Robot"""
    def __init__(self,electricity):
        self.electricity=electricity
        print(f'Amount: {electricity} ')
    """Attribute start"""
    def start(self):
        if self.electricity > 0:
            print('Status of your conection is: On')

        else:
            print('Status of your conection is: Off')
    """Attribute move"""
    def move(self):

        if self.electricity > 0:
            self.electricity -= 1
            print(f'It left {self.electricity}')
        else:
            print('It doesnt move')

class Date:
    """Init constructor"""
    def __init__(self):
        self.__day= 1

    def getDay(self):
        return self.__day

    def setDay(self,day):
        if day > 0 and day < 31:
            self.___day= day
            print(self.__day)
        else:
            print("Error")

    day= property(getDay,setDay)

class R2d2(Robot):
    """Class constructor R2d2"""
    def __init__(self,weapon,electricity):
        """Inherited attribute"""
        Robot.__init__(self,electricity)
        self.weapon=weapon
        print(f' Your weapon is {weapon} and your energy is {electricity}')

    
if __name__ == "__main__":
    my_robot= Robot(int(input('Write the amount of electricity: ')))
    my_robot.start()    
    my_robot.move()
    r1=R2d2(input('Write the type of weapon: '),int(input('Write the amount of electricity: ')))
    r1.start()
    r1.move()
    my_date=Date()
    my_date.day= int(input('Write the exact day:'))


    

