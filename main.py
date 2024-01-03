import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))