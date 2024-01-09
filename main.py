import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import sklearn.datasets
print(sklearn.datasets.load_iris())