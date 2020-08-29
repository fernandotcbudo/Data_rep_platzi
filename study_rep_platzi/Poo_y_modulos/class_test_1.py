#POO Test 

class bicycle():

    wells=2

    def moving(self):
        print('The bicycle starts to move')


class car():

    wells=4

    def moving(self):
        print('The car starts to move')



my_bike=bicycle()

print(f'My bike has {my_bike.wells} wells')

my_car=car()

print(f'My car has {my_car.wells} wells')

print('-----------------------------------------')

if __name__ == "__main__":
    my_bike.moving()
    my_car.moving()
