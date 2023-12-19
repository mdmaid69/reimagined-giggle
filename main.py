import shutil
def move_file(src, dst):
        shutil.move(src, dst)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])