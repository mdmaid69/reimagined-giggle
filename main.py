import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def calculate_force(mass, acceleration):
        return mass * acceleration