def count_characters(sentence):
        return len(sentence)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)