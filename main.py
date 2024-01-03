def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)