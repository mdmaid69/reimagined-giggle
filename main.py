import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)