sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)