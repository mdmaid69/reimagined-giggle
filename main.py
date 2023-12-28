import shutil
def delete_directory(path):
        shutil.rmtree(path)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))