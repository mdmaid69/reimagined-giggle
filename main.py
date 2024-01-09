def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)