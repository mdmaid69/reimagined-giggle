import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import shutil
def delete_directory(path):
        shutil.rmtree(path)