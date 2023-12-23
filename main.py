import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())