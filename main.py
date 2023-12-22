import sklearn.datasets
print(sklearn.datasets.load_iris())
import os
def get_file_size(filename):
        return os.path.getsize(filename)