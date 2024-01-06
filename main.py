def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import shutil
def move_file(src, dst):
        shutil.move(src, dst)