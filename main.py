import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def convert_to_octal(n):
        return oct(n)