class pet:
    def __init__(self):
        pass
    def set_name(self,name):
        self.__name = name
    def animal_type(self,animal_type):
        self.__animal_type = animal_type
    def set_age(self,age):
        self.__age = age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    def __str__(self):
        return f'{self.get_name()} is a {self.get_animal_type()} that is {self.get_age()} years old'
    
def main():
    obj1 = pet()
    name = input('Enter name of your pet: ')
    obj1.set_name(name)
    type = input('What animal is your pet? ')
    obj1.animal_type(type)
    try:
        age = int(input('How old is it? '))
        obj1.set_age(age)
    except:
        print('Age should be an integer')
    
    print('Pet Details :')
    # obj1.get_name()
    # obj1.get_animal_type()
    # obj1.get_age()
    print(obj1)

if __name__ == '__main__':
    main()
    
    
