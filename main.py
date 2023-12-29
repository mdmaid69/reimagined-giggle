import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets