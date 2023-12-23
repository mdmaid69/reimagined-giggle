import sys
def exit_program():
        sys.exit()
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)