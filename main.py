import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list