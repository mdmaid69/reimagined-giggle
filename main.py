import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import getpass
def get_username():
        return getpass.getuser()