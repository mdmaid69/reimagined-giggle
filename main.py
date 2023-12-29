import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)