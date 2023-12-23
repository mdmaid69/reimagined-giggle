n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)