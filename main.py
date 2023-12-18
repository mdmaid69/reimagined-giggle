import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities