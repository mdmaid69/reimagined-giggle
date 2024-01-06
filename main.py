import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import sys
def print_python_version():
        print(sys.version)