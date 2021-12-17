#Exercise to practice POO heritance

class father():


    def __init__ (self,eyes,hair):
        self.eyes=eyes
        self.hair=hair


    def drive_car(self):
        print('This person knows how to drive a car')

class son(father):

    def drive_bike(self):
        print('This person knows how to drive a bike')

person=son('Brown','Black')

if __name__ == "__main__":
    print(f'The eyes of this person are {person.eyes}')
    print(f'The hair of this person is {person.hair}')
    person.drive_bike()
    person.drive_car()

