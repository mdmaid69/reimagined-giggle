import glob
def find_files(pattern):
        return glob.glob(pattern)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b