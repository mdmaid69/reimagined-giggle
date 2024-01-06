import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)