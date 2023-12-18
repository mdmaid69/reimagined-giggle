def convert_to_binary(n):
        return bin(n)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)