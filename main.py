import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()