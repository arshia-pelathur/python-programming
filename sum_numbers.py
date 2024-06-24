import random 
number = random.randint(1,10)

def summing_up(number):
    value = 1
    sum = 0
    while value<=number:
        sum = sum+value
        value+=1
    return sum
    
ans = summing_up(number)
print(f'Sum of the first {number} positive digits are','---->',ans)
