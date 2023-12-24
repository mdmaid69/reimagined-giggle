import collections
def create_queue():
        return collections.deque()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)