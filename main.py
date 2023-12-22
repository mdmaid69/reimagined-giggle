import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import shutil
def delete_directory(path):
        shutil.rmtree(path)