def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)