import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)