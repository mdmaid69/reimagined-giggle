import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity