#POO CLASES OBJECTS - HERITAGE
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

    

