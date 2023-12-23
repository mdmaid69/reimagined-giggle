def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)