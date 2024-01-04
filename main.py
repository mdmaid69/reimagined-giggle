import shutil
def move_file(src, dst):
        shutil.move(src, dst)
n = 10
print("Powers of 2:", [2**x for x in range(n)])