import shutil
def delete_directory(path):
        shutil.rmtree(path)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))