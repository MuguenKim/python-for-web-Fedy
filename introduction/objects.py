import datetime


class Human():
    def __init__(self, name, year, gender):
        self.name = name
        self.year = year
        self.gender = gender

    def getAge(self):
        return datetime.datetime.now().year - self.year

    # def __str__(self):
    #     return 'name: ' + self.name + ' ,age: ' + str(self.year)+' ,gender: '+self.gender


h1 = Human("Fedy", 1992, "M")
