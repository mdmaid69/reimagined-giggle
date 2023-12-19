import collections
def create_stack():
        return collections.deque()
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])