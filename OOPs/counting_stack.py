class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.sum = 0

    def get_sum(self):
        return self.sum
    
    def get_counter(self):
        return self.count

    def pop(self):
        self.count+=1
        val = Stack.pop(self)
        self.sum += val
        return val
	

stk = CountingStack()
for i in range(15):
    print(i,end='  ')
    stk.push(i)
    stk.pop()
    
print()
print('Number of elements in Stack: ',stk.get_counter())
print('Sum of all elements in stack: ',stk.get_sum())
