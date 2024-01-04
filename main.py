import sklearn.datasets
print(sklearn.datasets.load_iris())
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)