def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))