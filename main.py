import shutil
def delete_directory(path):
        shutil.rmtree(path)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b