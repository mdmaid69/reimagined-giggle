n = 10
print("Square numbers:", [x**2 for x in range(n)])
import shutil
def move_file(src, dst):
        shutil.move(src, dst)