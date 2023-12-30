n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import shutil
def move_file(src, dst):
        shutil.move(src, dst)