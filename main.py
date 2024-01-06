import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import collections
def create_stack():
        return collections.deque()