import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)