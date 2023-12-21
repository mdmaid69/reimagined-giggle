def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))