import collections
def create_stack():
        return collections.deque()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)