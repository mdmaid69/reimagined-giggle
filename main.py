import shutil
def delete_directory(path):
        shutil.rmtree(path)
import sklearn.datasets
print(sklearn.datasets.load_iris())