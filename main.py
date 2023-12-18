import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_volume(length, width, height):
        return length * width * height