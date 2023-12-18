import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets