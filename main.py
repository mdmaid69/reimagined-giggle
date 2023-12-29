import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue