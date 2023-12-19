import os
def list_files_in_directory(path):
        return os.listdir(path)
import sklearn.datasets
print(sklearn.datasets.load_iris())