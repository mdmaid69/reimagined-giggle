import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper