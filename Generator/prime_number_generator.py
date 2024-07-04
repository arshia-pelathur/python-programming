import math

def generate_prime():
    value = 2        # smallest prime number
    while True:
        if all(value %x !=0 for x in range(2,int(math.sqrt(value))+1)):
            yield value
        value+=1

prime = generate_prime()
for _ in range(18):
    print(next(prime))