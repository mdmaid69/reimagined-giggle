import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def calculate_roi(gain, cost):
        return (gain - cost) / cost