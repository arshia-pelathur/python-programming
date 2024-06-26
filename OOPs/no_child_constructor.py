class Jedi:

    def __init__(self,force,name):
        self.force = force + 100
        self.name = name
    def __str__(self):
        return 'This is the parent calss- Jedi'
    
class Padawan(Jedi):
    def __str__(self):
        return 'This is the child class - Padwan'
    

player1 = Jedi(45,'Luke')
player2 = Padawan(23,'Ben')

print(player1.force)
print(player2.force)