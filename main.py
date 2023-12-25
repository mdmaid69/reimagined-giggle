import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import sklearn.datasets
print(sklearn.datasets.load_iris())