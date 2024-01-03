import sys
def add_to_python_path(path):
        sys.path.append(path)
import sklearn.datasets
print(sklearn.datasets.load_iris())