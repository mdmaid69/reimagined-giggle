import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)