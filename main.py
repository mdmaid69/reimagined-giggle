import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import sklearn.datasets
print(sklearn.datasets.load_iris())