import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))