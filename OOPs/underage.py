class Information:
    def __init__(self,name,address,age,number,sex):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__number = number
        self.__gender = sex
    
    def check_age(self):
        if self.__age >= 18:
            return 'yes'
        else:
            return 'no'

class Underage(Information):

    def __init__(self,name,address,age,number,sex):
        super().__init__(name,address,age,number,sex)
        if self._Information__age >=18:
            raise ValueError('Age of a minor should be less than 18 years')
    
    def check_age(self):
        return super().check_age()
    
person1 = Information('Maria','Toronto',29,4567891234,'F')
setattr(person1,'_Information__drinking',person1.check_age())
setattr(person1,'_Information__driving',person1.check_age())
setattr(person1,'_Information__voting',person1.check_age())

print('\nIndividual Information:\n',person1.__dict__)
try:
    person2 = Underage('David','Vanouver',15,4067391229,'M')
    setattr(person2,'_Underage__drinking',person2.check_age())
    setattr(person2,'_Underage__driving',person2.check_age())
    setattr(person2,'_Underage__voting',person2.check_age())

    print('\nIndividual is Underage:\n',person2.__dict__)
except ValueError as e:
    print(e)