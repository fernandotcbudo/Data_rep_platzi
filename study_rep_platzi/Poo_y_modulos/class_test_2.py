#Exercise to practice Polymorphism and methods of the classes

class dog():

    def __init__(self,race,color,name):
        self.race=race
        self.color=color
        self.name=name

    def __str__(self):
        return """\
            Race: {}
            Name: {}
            Color:{}""".format(self.race,self.name,self.color)



lucas= dog('Criollo','black with white hair','lucas')



if __name__ == "__main__":
    print(lucas)
