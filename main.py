import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)