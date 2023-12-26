import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import sklearn.datasets
print(sklearn.datasets.load_iris())