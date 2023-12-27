import collections
def create_queue():
        return collections.deque()
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])