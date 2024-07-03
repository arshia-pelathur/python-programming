class Fibonacci:
    def __init__(self, num):
        print("__init__")
        self.__n = num
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration()
        elif self.__i in [1, 2]:
            return 1
        else:
            ret = self.__p1 + self.__p2
            self.__p1, self.__p2 = self.__p2, ret
            return ret


for i in Fibonacci(12):
    print(i)

