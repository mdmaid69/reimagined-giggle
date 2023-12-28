import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)