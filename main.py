import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import sklearn.datasets
print(sklearn.datasets.load_iris())