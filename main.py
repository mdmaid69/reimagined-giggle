import sys
def exit_program():
        sys.exit()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)