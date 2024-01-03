import collections
def create_queue():
        return collections.deque()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)