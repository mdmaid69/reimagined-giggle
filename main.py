import collections
def create_counter():
        return collections.Counter()
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])