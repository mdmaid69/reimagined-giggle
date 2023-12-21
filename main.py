import shutil
def delete_directory(path):
        shutil.rmtree(path)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))