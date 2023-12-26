def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))