import sys
def add_to_python_path(path):
        sys.path.append(path)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)