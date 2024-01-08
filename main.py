import sklearn.datasets
print(sklearn.datasets.load_iris())
import os
def remove_directory(path):
        os.rmdir(path)