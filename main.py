import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)