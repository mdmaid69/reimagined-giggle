import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities