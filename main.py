import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)