import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import glob
def find_files(pattern):
        return glob.glob(pattern)