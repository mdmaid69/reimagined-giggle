numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)