#Encapsulation exercise

class Example():

    def __init__(self):
        self.hidden='Hidden'

    def public (self):
        return'Im a public method'

    def __private (self):
        return('Im a private method')

    def get_hidden(self):
        return self.hidden

    def set_hidden(self):
        self._hidden=self.__private()


    
object=Example()


if __name__ == "__main__":
    print(object.public())
    print(object._Example__private())
    print(object.get_hidden())
    print(object.set_hidden())