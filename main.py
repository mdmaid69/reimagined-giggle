def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import collections
def create_stack():
        return collections.deque()