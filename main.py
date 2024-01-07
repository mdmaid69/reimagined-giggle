n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import shutil
def move_file(src, dst):
        shutil.move(src, dst)