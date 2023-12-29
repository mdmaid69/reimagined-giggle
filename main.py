import sklearn.datasets
print(sklearn.datasets.load_iris())
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)