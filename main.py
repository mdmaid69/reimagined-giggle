import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import sklearn.datasets
print(sklearn.datasets.load_iris())