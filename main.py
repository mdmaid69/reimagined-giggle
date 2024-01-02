import sklearn.datasets
print(sklearn.datasets.load_iris())
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)