def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])