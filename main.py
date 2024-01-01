def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))