import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import sklearn.datasets
print(sklearn.datasets.load_iris())