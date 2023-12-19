import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_volume(length, width, height):
        return length * width * height