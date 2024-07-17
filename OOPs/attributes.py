from underage import Information,Underage


# Creating an instance of Information
person1 = Information('Maria', 'Toronto', 29, 4567891234, 'F')
setattr(person1,'_Information__drinking',person1.check_age())
setattr(person1,'_Information__driving',person1.check_age())
setattr(person1,'_Information__voting',person1.check_age())

print('\nIndividual Information:\n',person1.__dict__)
# Creating an instance of Underage
try:
    person2 = Underage('David', 'Vancouver', 17, 4067391229, 'M')
    setattr(person2,'_Underage__drinking',person2.check_age())
    setattr(person2,'_Underage__driving',person2.check_age())
    setattr(person2,'_Underage__voting',person2.check_age())

    print('\nIndividual is Underage:\n',person2.__dict__)
except ValueError as e:
    print(e)

print(list(person2.__dict__.keys()))
for name in list(person1.__dict__.keys()) + (list(person2.__dict__.keys())):
    att = name.split('__')[-1]
    try:
        if att.startswith('v'):
            val = getattr(person1,name)
            if val == 'yes': print('You are an Adult. You can vote.')
            else: print('Still a child. Can\'t vote')
    except:
        pass