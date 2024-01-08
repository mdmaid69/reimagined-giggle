def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
i = 0
while i < 5:
        print(i)
        i += 1