import random

list1 = [random.randint(1,30) for _ in range(10)]
triples = list(map(lambda num:num*3,list1))

print(list1,triples,sep='\n\n')