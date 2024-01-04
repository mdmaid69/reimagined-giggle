import random
def roll_die():
        return random.randint(1, 6)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)