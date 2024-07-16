import random

print([random.randrange(1,13) for _ in range(10)])
print([random.randint(1,10) for _ in range(10)])
print(random.choice([item for item in range(10)]))

l = [random.randint(1,100) for item in range(10)]
print(l)
print(random.choices(l,k=15,weights = [10,8,0,1,0,0,0,0,1,0]))
print(random.sample(l,k=5))