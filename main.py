import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))