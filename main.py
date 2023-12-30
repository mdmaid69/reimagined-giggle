import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import getpass
def get_username():
        return getpass.getuser()