import shutil
def delete_directory(path):
        shutil.rmtree(path)
import collections
def create_priority_queue():
        return collections.deque()