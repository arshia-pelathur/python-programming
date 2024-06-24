def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

factorial = [fact(number) for number in range(1,11)]

print(factorial)