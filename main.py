import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity