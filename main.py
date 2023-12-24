import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_acceleration(speed, time):
        return speed / time