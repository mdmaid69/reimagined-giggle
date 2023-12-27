def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)