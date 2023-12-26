import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def reverse_string(s):
        return s[::-1]