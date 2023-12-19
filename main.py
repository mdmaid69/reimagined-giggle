import collections
def create_queue():
        return collections.deque()
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)