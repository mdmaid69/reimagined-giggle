import shutil
def delete_directory(path):
        shutil.rmtree(path)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)