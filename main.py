import collections
def create_queue():
        return collections.deque()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b