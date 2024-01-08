import shutil
def delete_directory(path):
        shutil.rmtree(path)
import collections
def create_queue():
        return collections.deque()