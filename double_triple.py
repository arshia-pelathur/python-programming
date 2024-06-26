import numpy as np
import random


lst = [random.randint(1,20) for _ in range(20)]
print(lst)

sol = [val*2 if val%2 == 0 else val*3 for val in lst if (val*2 if val%2 == 0 else val*3) > 10]

print(sol)