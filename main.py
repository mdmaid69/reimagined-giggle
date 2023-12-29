import tensorflow as tf
print(tf.__version__)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)