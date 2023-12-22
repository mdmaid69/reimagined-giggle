import collections
def create_stack():
        return collections.deque()
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])