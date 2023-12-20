import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def find_unique_words(sentence):
        return set(sentence.split())