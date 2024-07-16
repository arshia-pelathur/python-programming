# FIFO - First In First Out



import random

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0,elem)

    def get(self):
        value = self.__queue[-1]
        del self.__queue[-1]
        return value


object = Queue()

for _ in range(5):
    item = random.randrange(1,16)
    object.put(item)
    print('In Queue - ',item)

print('\nFirst In First Out:\n')
for _ in range(len(object._Queue__queue)):
    print(object.get())