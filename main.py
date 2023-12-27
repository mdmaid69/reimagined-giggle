import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets