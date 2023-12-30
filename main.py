import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import re
def split_string(pattern, string):
        return re.split(pattern, string)