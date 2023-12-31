def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)