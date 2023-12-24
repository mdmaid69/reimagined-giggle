import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)