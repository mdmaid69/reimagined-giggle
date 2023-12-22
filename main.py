import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)