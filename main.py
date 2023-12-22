import shutil
def delete_directory(path):
        shutil.rmtree(path)
import collections
def create_stack():
        return collections.deque()