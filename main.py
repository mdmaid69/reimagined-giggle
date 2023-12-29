def count_words(sentence):
        return len(sentence.split())
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)