import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)