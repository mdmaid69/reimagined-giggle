import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)