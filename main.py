import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import random
def generate_random_number(start, end):
        return random.randint(start, end)