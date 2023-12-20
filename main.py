import sklearn.datasets
print(sklearn.datasets.load_iris())
import re
def split_string(pattern, string):
        return re.split(pattern, string)