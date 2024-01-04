import shutil
def delete_directory(path):
        shutil.rmtree(path)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)