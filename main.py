import sklearn.datasets
print(sklearn.datasets.load_iris())
import shutil
def delete_directory(path):
        shutil.rmtree(path)