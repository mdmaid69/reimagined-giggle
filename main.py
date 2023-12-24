import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)