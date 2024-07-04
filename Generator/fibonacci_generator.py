def fib(n):
    p1 = 0
    p2 = p3 = 1
    for i in range(n):
        if i == 0:
            yield i
        elif i in [1,2]:
            yield 1
        else:
            yield p2+p3
            p2,p3 = p3,p2+p3

values = list(fib(15))
print(values)