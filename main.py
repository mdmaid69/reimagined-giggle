import shutil
def delete_directory(path):
        shutil.rmtree(path)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))