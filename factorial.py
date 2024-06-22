def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter a number to calculate factorial: "))
factorial_ans = fact(n)

print(factorial_ans)