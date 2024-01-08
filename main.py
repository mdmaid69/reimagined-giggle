import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets