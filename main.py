import sklearn.datasets
print(sklearn.datasets.load_iris())
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)