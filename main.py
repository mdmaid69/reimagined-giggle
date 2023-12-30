import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import getpass
def get_username():
        return getpass.getuser()