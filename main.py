n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)