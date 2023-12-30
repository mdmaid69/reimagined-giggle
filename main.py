def reverse_string(s):
        return s[::-1]
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)