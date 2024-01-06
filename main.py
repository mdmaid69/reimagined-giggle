import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets