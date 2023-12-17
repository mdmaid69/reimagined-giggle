for i in range(5):
        print(i)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)