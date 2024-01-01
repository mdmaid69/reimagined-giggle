import glob
def find_files(pattern):
        return glob.glob(pattern)
import sklearn.datasets
print(sklearn.datasets.load_iris())