def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))