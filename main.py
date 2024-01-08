def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))