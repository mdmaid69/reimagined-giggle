import itertools
print(list(itertools.permutations([1, 2, 3])))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)