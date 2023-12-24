import collections
def create_priority_queue():
        return collections.deque()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)