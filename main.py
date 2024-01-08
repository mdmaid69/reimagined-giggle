n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)