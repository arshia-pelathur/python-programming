import random
l1 = [random.randint(1,10) for _ in range(5)]
l2 = [random.randint(1,10) for _ in range(5)]
l3 = [random.randint(1,10) for _ in range(5)]

sumlist = list(map(lambda x,y,z : x+y+z,l1,l2,l3))

print(l1,l2,l3,sumlist,sep='\n')