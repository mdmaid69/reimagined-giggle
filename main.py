import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
n = 10
print("Powers of 2:", [2**x for x in range(n)])