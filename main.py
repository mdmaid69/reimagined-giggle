import glob
def find_files(pattern):
        return glob.glob(pattern)
import collections
def create_stack():
        return collections.deque()