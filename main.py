import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_pressure(force, area):
        return force / area