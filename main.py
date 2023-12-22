def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)