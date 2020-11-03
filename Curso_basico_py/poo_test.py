class Robot:
    def __init__(self,electricity):
        self.electricity=electricity
        print(f'Amount: {electricity} ')

    def start(self):
        if self.electricity > 0:
            print('Status of your conection is: On')

        else:
            print('Status of your conection is: Off')

    def move(self):

        if self.electricity > 0:
            self.electricity -= 1
            print(f'It left {self.electricity}')
        else:
            print('It doesnt move')


if __name__ == "__main__":
    my_robot= Robot(int(input('Write the amount of electricity: ')))
    my_robot.start()    
    my_robot.move()

