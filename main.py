def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))