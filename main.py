import collections
def create_queue():
        return collections.deque()
import glob
def find_files(pattern):
        return glob.glob(pattern)