import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_density(mass, volume):
        return mass / volume