import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b