def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)