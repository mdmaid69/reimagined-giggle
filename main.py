import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import sklearn.datasets
print(sklearn.datasets.load_iris())