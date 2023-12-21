def calculate_volume(length, width, height):
        return length * width * height
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)