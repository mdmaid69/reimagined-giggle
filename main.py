import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets