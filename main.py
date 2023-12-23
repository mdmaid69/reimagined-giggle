import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import shutil
def move_file(src, dst):
        shutil.move(src, dst)