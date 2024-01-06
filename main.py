import sklearn.datasets
print(sklearn.datasets.load_iris())
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)