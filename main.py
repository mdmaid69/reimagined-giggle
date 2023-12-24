def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)