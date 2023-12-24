n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)