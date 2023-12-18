import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import shutil
def delete_directory(path):
        shutil.rmtree(path)