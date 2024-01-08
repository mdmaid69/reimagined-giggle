import random
def generate_random_choice(choices):
        return random.choice(choices)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)