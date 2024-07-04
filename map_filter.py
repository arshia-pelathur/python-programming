squares = list(map(lambda i:i*i,[i for i in range(1,21)]))
print(squares)


import math
squares_odd = list(filter(lambda x: x%2!=0,squares))
print(squares_odd)
