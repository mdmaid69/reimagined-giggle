n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)