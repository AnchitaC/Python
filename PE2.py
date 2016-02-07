def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

total = 0
n = 1
while fib(n)  <= 4000000:
    if fib(n) % 2 == 0:
        total = total + fib(n)
    n = n + 1
print(total)


