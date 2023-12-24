import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)