import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))