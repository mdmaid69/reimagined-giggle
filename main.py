import itertools
print(list(itertools.permutations([1, 2, 3])))
import shutil
def delete_directory(path):
        shutil.rmtree(path)