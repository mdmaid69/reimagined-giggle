import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets