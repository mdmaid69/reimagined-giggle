import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a