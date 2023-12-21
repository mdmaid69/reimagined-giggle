import shutil
def move_file(src, dst):
        shutil.move(src, dst)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b