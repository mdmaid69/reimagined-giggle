import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import shutil
def delete_directory(path):
        shutil.rmtree(path)