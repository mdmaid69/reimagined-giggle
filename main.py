import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import sklearn.datasets
print(sklearn.datasets.load_iris())