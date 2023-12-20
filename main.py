import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import itertools
print(list(itertools.permutations([1, 2, 3])))