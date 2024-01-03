n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)