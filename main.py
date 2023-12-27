import shutil
def delete_directory(path):
        shutil.rmtree(path)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))