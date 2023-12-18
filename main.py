import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h