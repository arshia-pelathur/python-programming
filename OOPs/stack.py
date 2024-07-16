# LIFO - Last In First Out
import random
class Stack:

    def __init__(self):
        self.__stck = []

    def push(self,ele):
        self.__stck.append(ele)
    
    def pop(self):
        value = self.__stck[-1]
        del self.__stck[-1]
        return value
    
object = Stack()

for _ in range(5):
    item = random.randrange(1,16)
    object.push(item)
    print('In Stack - ',item)

print('\nLast In First Out:\n')
for _ in range(len(object._Stack__stck)):
    print(object.pop())
