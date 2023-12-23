import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_speed(distance, time):
        return distance / time