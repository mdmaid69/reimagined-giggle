import os
def change_working_directory(path):
        os.chdir(path)
import sklearn.datasets
print(sklearn.datasets.load_iris())