import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)